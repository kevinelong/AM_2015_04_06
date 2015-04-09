#!/usr/bin/python

class Board(object):
	
	def __init__(self):
		self.board_file_nm	= 'board.json'
		self.game_file_nm	= 'game.json'
		self.__board_width 	= 3
		self.__board_height 	= 3
		self.__empty_spc	= '*'
		self.__playr1_symbol	= 'X'
		self.__playr2_symbol    = 'O'

	def get_game_status(self):
		try:
			v_game_dict = self.get_json('game')
		except IOError:
			self.get_new_board()

		if 	v_game_dict['game status']=='Over':
			self.get_new_board()
		else:
			v_input_str = "A game exists.  Would you like to continue? (Y/N) "
			v_continue_game = raw_input(v_input_str)
			v_continue_game	= v_continue_game.upper()

			if v_continue_game.upper()== 'N':
				print "Lets start a new game!"
				self.get_new_board()
			elif v_continue_game.upper() == 'Y':
				print "Last Game Loaded"
				self.print_board()
		                v_last_player   = v_game_dict['last player']
        		        v_turn_status   = v_game_dict['turn status']
				v_player_dict	= self.get_player_dict(v_last_player,v_turn_status)
		                v_player_no     = v_player_dict['player_no']
        	        	v_player_symbol = self.get_player_symbol(v_player_no)
                	        v_input_str   = "Player %s please select a row and column to place your %s (i.e. 2,2) " %(v_player_no,v_player_symbol)
	                        self.print_input(v_input_str)
			else:	
				print "Please enter a 'Y' to load previous game or a'N' to start a new game"
				self.get_game_status()
	
	def get_new_board(self):
		v_board_dict	= {}
		v_game_dict	= {}
		v_game_dict['game status']='ACT'
		v_game_dict['last player']=1
		v_game_dict['turn status']='Move'
		v_height_loop	= 0
		while v_height_loop <= self.__board_height:
			v_row_dict      = {}
			v_width_loop    = 0
			while v_width_loop <= self.__board_width:
				if v_height_loop == 0:
					if v_width_loop == 0:
						v_row_dict[0]='#'
					else:
						v_row_dict[v_width_loop]=v_width_loop
				else:
					if v_width_loop == 0:
						v_row_dict[0]=v_height_loop
					else:
						v_row_dict[v_width_loop] = self.__empty_spc
				v_width_loop    = v_width_loop+1
			v_board_dict[v_height_loop]=v_row_dict
			v_height_loop = v_height_loop+1

		self.write_json('board',v_board_dict)
		self.write_json('game',v_game_dict)
		self.print_board()
		v_input_str   = "Player 1 please select a row and column to place your %s (i.e. 2,2) " %(self.__playr1_symbol)
		self.print_input(v_input_str)

	def write_json(self,p_type,p_dict):
		import json	
		if p_type == 'board':
			v_file_nm = self.board_file_nm
		elif    p_type == 'game':
			v_file_nm = self.game_file_nm
		v_json_str  = json.dumps(p_dict)
		file_obj = open(v_file_nm,'w')
		file_obj.write(json.dumps(p_dict))
		file_obj.close

	def get_json(self,p_type):
		import json
		if 	p_type == 'board':
                        v_file_nm = self.board_file_nm
		elif 	p_type == 'game':
			v_file_nm = self.game_file_nm
		file_obj = open(v_file_nm,'r')
		v_json_str = file_obj.read()
		file_obj.close
		v_board = json.loads(v_json_str)

		return v_board

	def print_board(self):
		v_board_dict = self.get_json('board')
		v_height_loop   = 0
		while v_height_loop <= self.__board_height:
			v_dict_row 	= v_board_dict[str(v_height_loop)]
			v_width_loop    = 0
			v_print_row 	= ""
			while v_width_loop <= self.__board_width:
				v_col = v_dict_row[str(v_width_loop)]
				v_print_row = "%s  %s" %(v_print_row,v_col)
				v_width_loop    = v_width_loop+1
			print "%s\n" %(v_print_row.strip(' | '))
			v_height_loop = v_height_loop+1

	def chk_row_col(self,p_row,p_col):
		if p_row >= 1 and p_row <= self.__board_height and p_col >= 1 and p_col <= self.__board_width:
			v_val = 0
		elif p_row >= 1 and p_row > self.__board_height:
			v_val = -1
		elif p_col >= 1 and p_col > self.__board_width:
			v_val = -2

		return v_val

	def get_value(self,p_row,p_col):
		v_board_dict = self.get_json('board')
		if self.chk_row_col(p_row,p_col) == 0:
			v_row_dict	= v_board_dict[str(p_row)]
			v_val 		= v_row_dict[str(p_col)]
		else: 
			v_val = -1

		return v_val 

	def get_player_symbol(self,p_player_no):
		if 	p_player_no == 1:
			v_player_symbol = self.__playr1_symbol
		elif 	p_player_no == 2:
			v_player_symbol = self.__playr2_symbol
		else:
			v_player_symbol = -1
		return v_player_symbol

	def print_input(self,p_input_str):
		try:
			v_row_col_str 	= input(p_input_str)
			self.post_board(v_row_col_str[0],v_row_col_str[1])
		except:
			print "Please try again with two valid numbers seperated by a comma"
	               	v_game_dict     = self.get_json('game')
        	       	v_last_player   = v_game_dict['last player']
                	v_turn_status   = v_game_dict['turn status']
	                v_player_dict   = self.get_player_dict(v_last_player,v_turn_status)
                	v_player_no     = v_player_dict['player_no']
	                v_player_symbol = self.get_player_symbol(v_player_no)
                        v_input_str	= "Player %s please select a row and column to place your %s (i.e. 2,2) " %(v_player_no,v_player_symbol)
                        self.print_input(v_input_str)
		
	def get_player_dict(self,p_last_player,p_turn_status):
                if      p_last_player == 1 and p_turn_status == 'Move':
                        v_player_no             = 1
                        v_next_player_no        = 2
                elif    p_last_player == 1 and p_turn_status == 'Done':
                        v_player_no             = 2
                        v_next_player_no        = 1
                elif    p_last_player == 2 and p_turn_status == 'Move':
                        v_player_no             = 2
                        v_next_player_no        = 1
                elif    p_last_player == 2 and p_turn_status == 'Done':
                        v_player_no             = 1
                        v_next_player_no        = 2
		
		v_player_dict ={}
		v_player_dict['player_no']=v_player_no
		v_player_dict['next_player_no']=v_next_player_no
	
		return v_player_dict

	def chck_row_winner(self,p_board_dict):
		v_row_num 	= 1
		v_empty_spc_cnt	= 0
		v_plyr1_win_flg	= -1
		v_plyr2_win_flg = -1
		v_tie_flg	= -1
		v_row_win_dict	= {}

		while v_row_num <= self.__board_height: 
			v_dict_row = p_board_dict[str(v_row_num)]
			v_col_num       = 1
			v_playr1_cnt    = 0
			v_playr2_cnt    = 0

			while v_col_num <= self.__board_width:
				v_val = v_dict_row[str(v_col_num)]
				if  v_val == self.__playr1_symbol:
					v_playr1_cnt = v_playr1_cnt +1
				elif v_val == self.__playr2_symbol:
					v_playr2_cnt = v_playr2_cnt +1
				elif v_val == self.__empty_spc:
					v_empty_spc_cnt = v_empty_spc_cnt+1
			
				if 	v_playr1_cnt == self.__board_width:
					v_plyr1_win_flg = 0
					v_col_num = self.__board_width +1
					v_row_num = self.__board_height +1
				elif	v_playr2_cnt == self.__board_width:
					v_plyr2_win_flg = 0
					v_col_num = self.__board_width +1
					v_row_num = self.__board_height +1
				else:
					v_col_num = v_col_num +1
		
			v_row_num = v_row_num +1

		if v_empty_spc_cnt == 0 and v_plyr1_win_flg == -1 and v_plyr2_win_flg == -1:
			v_tie_flg = 0		

		v_row_win_dict['plyr1_win_flg']=v_plyr1_win_flg
		v_row_win_dict['plyr2_win_flg']=v_plyr2_win_flg
		v_row_win_dict['tie_flg']=v_tie_flg

		return v_row_win_dict

	def chk_diag_lft_winner(self,p_board_dict):
		v_row_num       	= 1
		v_plyr1_win_flg 	= -1
		v_plyr2_win_flg 	= -1
		v_diag_lft_win_dict  	= {}
		v_playr1_cnt		= 0
		v_playr2_cnt		= 0

		while v_row_num <= self.__board_height:
			v_dict_row = p_board_dict[str(v_row_num)]
			
			v_val = v_dict_row[str(v_row_num)]

			if 	v_val == self.__playr1_symbol:
				v_playr1_cnt = v_playr1_cnt +1
			elif 	v_val == self.__playr2_symbol:
				v_playr2_cnt = v_playr2_cnt +1

			v_row_num = v_row_num +1

		if 	v_playr1_cnt == self.__board_height:
			v_plyr1_win_flg = 0
		elif 	v_playr2_cnt == self.__board_height:
			v_plyr2_win_flg = 0
	
		v_diag_lft_win_dict['plyr1_win_flg']=v_plyr1_win_flg
		v_diag_lft_win_dict['plyr2_win_flg']=v_plyr1_win_flg
	
		return v_diag_lft_win_dict

        def chk_diag_rght_winner(self,p_board_dict):
                v_row_num               = 1
                v_plyr1_win_flg         = -1
                v_plyr2_win_flg         = -1
                v_diag_rght_win_dict     = {}
                v_playr1_cnt            = 0
                v_playr2_cnt            = 0

                while v_row_num <= self.__board_height:
                        v_dict_row = p_board_dict[str(v_row_num)]

			v_col_key = (self.__board_width - v_row_num)+1
                        v_val = v_dict_row[str(v_col_key)]

                        if      v_val == self.__playr1_symbol:
                                v_playr1_cnt = v_playr1_cnt +1
                        elif    v_val == self.__playr2_symbol:
                                v_playr2_cnt = v_playr2_cnt +1

                        v_row_num = v_row_num +1

                if      v_playr1_cnt == self.__board_height:
                        v_plyr1_win_flg = 0
                elif    v_playr2_cnt == self.__board_height:
                        v_plyr2_win_flg = 0

                v_diag_rght_win_dict['plyr1_win_flg']=v_plyr1_win_flg
                v_diag_rght_win_dict['plyr2_win_flg']=v_plyr1_win_flg

                return v_diag_rght_win_dict


	def get_game_over_dict(self):
		game_over_dict = {}
		v_game_over_flg	= -1
		v_game_over_msg	= "Keep Playing"
		v_board_dict	= self.get_json('board')
		v_row_win_dict	= self.chck_row_winner(v_board_dict)		
		if 	v_row_win_dict['plyr1_win_flg'] == 0:
			v_game_over_flg = 0
			v_game_over_msg = "Player 1 Wins!"
		elif	v_row_win_dict['plyr2_win_flg'] == 0:
			v_game_over_flg = 0
			v_game_over_msg = "Player 2 Wins!"
		else:
			v_diag_lft_win_dict = self.chk_diag_lft_winner(v_board_dict)
			if      v_diag_lft_win_dict['plyr1_win_flg'] == 0:
				v_game_over_flg = 0
				v_game_over_msg = "Player 1 Wins!"
			elif	v_diag_lft_win_dict['plyr2_win_flg'] == 0:
				v_game_over_flg = 0
				v_game_over_msg = "Player 2 Wins!"
			else:
				v_diag_rght_win_dict = self.chk_diag_rght_winner(v_board_dict)
				if 	v_diag_rght_win_dict['plyr1_win_flg'] == 0:
					v_game_over_flg = 0
					v_game_over_msg = "Player 1 Wins!"
				elif	v_diag_rght_win_dict['plyr2_win_flg'] == 0:
					v_game_over_flg = 0
					v_game_over_msg = "Player 2 Wins!"
				elif	v_row_win_dict['tie_flg'] == 0:
					v_game_over_flg = 0
					v_game_over_msg = "The game is a draw"
		
		game_over_dict['game_over_flg']=v_game_over_flg
		game_over_dict['game_over_msg']=v_game_over_msg

		return game_over_dict

	def post_board(self,p_row,p_col):
		v_board_dict	= self.get_json('board')
		v_game_dict	= self.get_json('game')
		v_last_player	= v_game_dict['last player']
		v_turn_status	= v_game_dict['turn status']

		v_player_dict 		= self.get_player_dict(v_last_player,v_turn_status)
		v_player_no 		= v_player_dict['player_no']
		v_next_player_no	= v_player_dict['next_player_no']
		
		v_player_symbol 	= self.get_player_symbol(v_player_no)
		v_next_player_symbol 	= self.get_player_symbol(v_next_player_no)

		v_chk_val = self.chk_row_col(p_row,p_col)
		if v_chk_val == 0:
			v_value		= self.get_value(p_row,p_col)
			if 	v_value == self.__empty_spc:
				v_row_dict	= v_board_dict[str(p_row)]
				v_row_dict[p_col]=v_player_symbol
				v_board_dict[p_row]=v_row_dict
				v_game_dict['last player']= v_player_no
				v_game_dict['turn status']= 'Done'
				self.write_json('board',v_board_dict)
				self.write_json('game',v_game_dict)
				self.print_board()
				v_game_over_dict = self.get_game_over_dict()
				if 	v_game_over_dict['game_over_flg'] == -1:				
					v_input_str   = "Player %s please select a row and column to place your %s (i.e. 2,2) " %(v_next_player_no,v_next_player_symbol)
			                self.print_input(v_input_str)
				else:
					v_game_dict['game status']='Over'		
					self.write_json('game',v_game_dict)
					print v_game_over_dict['game_over_msg']
			else:
				v_input_str = "Player %s please select an unused space " %(v_player_no)
				self.print_input(v_input_str)	
		elif v_chk_val == -1:
			v_input_str = "Player %s please use a Row value between 1 and %s " %(v_player_no,self.__board_height)
			self.print_input(v_input_str)
		elif v_chk_val == -2:
			v_input_str = "Player %s please use a Column value between 1 and %s " %(v_player_no,self.__board_width)
			self.print_input(v_input_str)
