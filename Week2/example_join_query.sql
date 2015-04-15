SELECT polls_question.question_text,
  polls_choice.choice_text,
  polls_question.pub_date
FROM polls_question
LEFT JOIN polls_choice
ON  polls_choice.question_id = polls_question.id
WHERE polls_question.pub_date is NOT NULL
ORDER BY polls_question.pub_date DESC,
  polls_choice.choice_text;