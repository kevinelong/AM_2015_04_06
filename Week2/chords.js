var Chord = function () {
    var scale = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"];
    var scaleDictionary = {};

    for (var scaleIndex = 0; scaleIndex < scale.length; scaleIndex++) {
        var noteName = scale[scaleIndex];
        scaleDictionary[noteName] = scaleIndex;
    }
    var neck = ["E", "A", "D", "G", "B", "E"];
    neckFrets = {};

    for (var i = 0; i < neck.length; i++) {
        var neckNote = neck[i];
        var neckIndex = scaleDictionary[neckNote];
        var fretCount = 5;
        var neckNoteList = [];
        for (var x = 0; x < fretCount; x++) {
            var scaleNote = scale[(neckIndex + x) % scale.length];
            neckNoteList.push(scaleNote);
        }
        neckFrets[i] = neckNoteList
    }


    var getGeneric = function (noteName, offsets) {
        noteName = noteName.toUpperCase();
        var index = scaleDictionary[noteName];
        var output = [];
        for (var i = 0; i < offsets.length; i++) {
            var sum = index + offsets[i];
            var len = scale.length;
            output.push(scale[sum % len]);
        }
        return output
    };

    function Major(noteName) {
        return getGeneric(noteName, [0, 4, 7]);
    }

    function MajorSeven(noteName) {
        return getGeneric(noteName, [0, 4, 7, 11])
    }

    function Minor(noteName) {
        return getGeneric(noteName, [0, 3, 7]);
    }

    function MinorSeven(noteName) {
        return getGeneric(noteName, [0, 3, 7, 11])
    }

    function Augmented(noteName) {
        return getGeneric(noteName, [0, 4, 8]);
    }

    function Diminished(noteName) {
        return getGeneric(noteName, [0, 3, 6]);
    }

    return {
        scale: scale,
        Major: Major,
        MajorSeven: MajorSeven,
        Minor: Minor,
        MinorSeven: MinorSeven,
        Augmented: Augmented,
        Diminished: Diminished
    }

}();
chords = {};
for (var i = 0; i < Chord.scale.length; i++) {
    var note = Chord.scale[i];
    if (!chords.hasOwnProperty(note)) {
        chords[note] = {};
    }
    chords[note]["major"] = Chord.Major(note);
    chords[note]["major-seven"] = Chord.MajorSeven(note);
    chords[note]["minor"] = Chord.Minor(note);
    chords[note]["minor-seven"] = Chord.MinorSeven(note);
    chords[note]["augmented"] = Chord.Augmented(note);
    chords[note]["diminished"] = Chord.Diminished(note);

}

var map = {"major":"Major",
            "major-seven":"MajorSeven",
            "minor":"Minor",
            "minor-seven":"MinorSeven",
            "augmented":"Augmented",
            "diminished":"Diminished"
};
console.log(neckFrets);
    var getFrets = function(chordNoteList){
        var sf = [];
        for( var s in neckFrets){
            var fret = neckFrets[s];
            for (var fretIndex in fret){
                var fret_note = fret[fretIndex];
                if(chordNoteList.indexOf(fret_note) >= 0){
                    sf.push(fretIndex);
                    break;
                }
            }
        }
        return sf;
    };

var Update = function(){

    if(selectedType && selectedNote){
        var displayChord = Chord[map[selectedType]](selectedNote);
        var fingers = getFrets(displayChord)
        var output = [];
        for(var fp=1;fp<5;fp++){
            var line = "";
            for(var s=0;s<6;s++){
                if(fingers[s]==fp){
                    line += " O "
                }else{
                    line += " | "
                }
            }
            output.push(line)
        }

        document.getElementById("output").innerHTML = "<pre>" + output.join("<br>\n") + "</pre>";
    }
};


document.addEventListener("DOMContentLoaded", function (event) {
    var noteSelect = document.createElement("select");
        noteSelect.appendChild(document.createElement("option"));
    for (var i = 0; i < Chord.scale.length; i++) {
        var noteOption = document.createElement("option");
        noteOption.innerHTML = Chord.scale[i];
        noteSelect.appendChild(noteOption);
    }
    document.body.appendChild(noteSelect);

    noteSelect.addEventListener("change", function(event){
        window.selectedNote = event.target.value;
        Update();
    })
});

document.addEventListener("DOMContentLoaded", function (event) {
    var typeSelect = document.createElement("select");
    var openDisplay = document.createElement("option");
        typeSelect.appendChild(openDisplay);
    var keys = Object.keys(chords["A"]);

    for (var i = 0; i < keys.length; i++) {
        var key = keys[i];
        var typeOption = document.createElement("option");
        typeOption.innerHTML = key;
        typeSelect.appendChild(typeOption);
    }

    document.body.appendChild(typeSelect);

    typeSelect.addEventListener("change", function(event){
        window.selectedType = event.target.value;
        Update();
    })


});