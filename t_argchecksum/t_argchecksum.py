#Coading: UTF-8
from sys import version_info, exit, exc_info
from traceback import print_tb, format_exception_only

class MyCheckSum:

	def __init__(self, *arg):
		self.args = arg

	def common_checksum(function):
		def values(*args):
			try:
				# {ip_checksum}Function Get ReturnValue [{ip_checksum}関数のReturn値を取得]
				# Calculate One's Complement [1の補数を計算]
				# XOR Calculation [XOR計算]
				total_binary_nuber	= function(*args)
				binary_number		= (total_binary_nuber & 0xffff) + (total_binary_nuber >> 16)
				checksum_value		= binary_number ^ 0xffff
				return checksum_value
			except KeyboardInterrupt:
				print(f'\n\nProcess Interrupted [処理を中断しました]')
				exit(1)
			except:
				exc_type, exc_message, exc_object	= exc_info()
				exc_list							= format_exception_only(exc_type, exc_message)
				error_message						= ''.join(exc_message for exc_message in exc_list)
				print_tb(exc_object)
				print(f'  {error_message}')
				exit(1)
		return values

	@common_checksum
	def iptcp_header_module(self):
		try:
			# Python Version Check [Pythonバージョン確認]
			if version_info.major > 2:
				xrange = range
			
			# Initialization [初期設定]
			total_binary_nuber = 0
			
			# byte(Hexadecimal) => str(BinaryNumber) [バイト型(16進数) => 文字型(2進数)]
			binary_numbers = format(int.from_bytes(self.args[0], 'big'), '0160b')

			# Get Binary Length [バイナリの長さを取得]
			# [16ずつ値を取得し基数を２進数にし足していく]
			binary_numbers_len = int(len(binary_numbers))
			for get_length in xrange(0, binary_numbers_len, 16):
				total_binary_nuber += int(binary_numbers[get_length:get_length+16], 2)
			return total_binary_nuber
		except KeyboardInterrupt:
			print(f'\n\nProcess Interrupted [処理を中断しました]')
			exit(1)
		except:
			exc_type, exc_message, exc_object = exc_info()
			exc_list = format_exception_only(exc_type, exc_message)
			error_message = ''.join(exc_message for exc_message in exc_list)
			print_tb(exc_object)
			print(f'  {error_message}')
			exit(1)
