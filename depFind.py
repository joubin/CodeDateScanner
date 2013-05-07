import os
import sys
import time
from list import getCall
files = []
# deprecatedFunctions = ['define_syslog_variables\n', 'register_globals\n', 'register_long_arrays\n', 'safe_mode\n', 'magic_quotes_gpc\n', 'magic_quotes_runtime\n', 'magic_quotes_sybase\n', 'call_user_method  \n', 'call_user_method_array  \n', 'define_syslog_variables \n', 'dl \n', 'ereg  \n', 'ereg_replace  \n', 'eregi  \n', 'eregi_replace  \n', 'set_magic_quotes_runtime \n', 'magic_quotes_runtime \n', 'session_register  \n', 'session_unregister  \n', 'session_is_registered  \n', 'set_socket_blocking \n', 'split  \n', 'spliti  \n', 'sql_regcase \n', 'mysql_db_query \n', 'mysql_escape_string  \n', 'mcrypt_generic_end\n', 'mysql_list_dbs\n', '\n', '\n', 'exec          \n', 'passthru      \n', 'system        \n', 'shell_exec    \n', 'popen         \n', 'proc_open     \n', 'pcntl_exec\n', 'eval\n', 'assert\n', 'preg_replace\n', 'create_function\n', 'include\n', 'include_once\n', 'require\n', 'require_once\n', '$_GET\n', '\n', '\n', 'Function                   \n', "'ob_start'                 \n", "'array_diff_uassoc'        \n", "'array_diff_ukey'          \n", "'array_filter'             \n", "'array_intersect_uassoc'   \n", "'array_intersect_ukey'     \n", "'array_map'                \n", "'array_reduce'             \n", "'array_udiff_assoc'        \n", "'array_udiff_uassoc'       \n", "'array_udiff'              \n", "'array_uintersect_assoc'   \n", "'array_uintersect_uassoc'  \n", "'array_uintersect'         \n", "'array_walk_recursive'     \n", "'array_walk'               \n", "'assert_options'           \n", "'uasort'                   \n", "'uksort'                   \n", "'usort'                    \n", "'preg_replace_callback'    \n", "'spl_autoload_register'    \n", "'iterator_apply'           \n", "'call_user_func'           \n", "'call_user_func_array'     \n", "'register_shutdown_function\n", "'register_tick_function'   \n", "'set_error_handler'        \n", "'set_exception_handler'    \n", "'session_set_save_handler' \n", "'sqlite_create_aggregate'  \n", "'sqlite_create_function'  \n", '\n', 'phpinfo\n', 'posix_mkfifo\n', 'posix_getlogin\n', 'posix_ttyname\n', 'getenv\n', 'get_current_user\n', 'proc_get_status\n', 'get_cfg_var\n', 'disk_free_space\n', 'disk_total_space\n', 'diskfreespace\n', 'getcwd\n', 'getlastmo\n', 'getmygid\n', 'getmyinode\n', 'getmypid\n', 'getmyuid\n', '\n', '\n', 'extract\n', 'parse_str\n', 'putenv\n', 'ini_set\n', 'mail\n', 'header\n', 'proc_nice\n', 'proc_terminate\n', 'proc_close\n', 'pfsockopen\n', 'fsockopen\n', 'apache_child_terminate\n', 'posix_kill\n', 'posix_mkfifo\n', 'posix_setpgid\n', 'posix_setsid\n', 'posix_setuid \n', '\n', '// open filesystem handler\n', 'fopen\n', 'tmpfile\n', 'bzopen\n', 'gzopen\n', 'SplFileObject->__construct\n', '// write to filesystem (partially in combination with reading)\n', 'chgrp\n', 'chmod\n', 'chown\n', 'copy\n', 'file_put_contents\n', 'lchgrp\n', 'lchown\n', 'link\n', 'mkdir\n', 'move_uploaded_file\n', 'rename\n', 'rmdir\n', 'symlink\n', 'tempnam\n', 'touch\n', 'unlink\n', 'imagepng  \n', 'imagewbmp \n', 'image2wbmp\n', 'imagejpeg \n', 'imagexbm  \n', 'imagegif  \n', 'imagegd   \n', 'imagegd2  \n', 'iptcembed\n', 'ftp_get\n', 'ftp_nb_get\n', 'file_exists\n', 'file_get_contents\n', 'file\n', 'fileatime\n', 'filectime\n', 'filegroup\n', 'fileinode\n', 'filemtime\n', 'fileowner\n', 'fileperms\n', 'filesize\n', 'filetype\n', 'glob\n', 'is_dir\n', 'is_executable\n', 'is_file\n', 'is_link\n', 'is_readable\n', 'is_uploaded_file\n', 'is_writable\n', 'is_writeable\n', 'linkinfo\n', 'lstat\n', 'parse_ini_file\n', 'pathinfo\n', 'readfile\n', 'readlink\n', 'realpath\n', 'stat\n', 'gzfile\n', 'readgzfile\n', 'getimagesize\n', 'imagecreatefromgif\n', 'imagecreatefromjpeg\n', 'imagecreatefrompng\n', 'imagecreatefromwbmp\n', 'imagecreatefromxbm\n', 'imagecreatefromxpm\n', 'ftp_put\n', 'ftp_nb_put\n', 'exif_read_data\n', 'read_exif_data\n', 'exif_thumbnail\n', 'exif_imagetype\n', 'hash_file\n', 'hash_hmac_file\n', 'hash_update_file\n', 'md5_file\n', 'sha1_file\n', 'highlight_file\n', 'show_source\n', 'php_strip_whitespace\n', 'get_meta_tags']

depricatedFunctions = []
s = ''
def CheckAndSetFolder(f):
	if os.path.exists(f):
		os.chdir(f)
		flag = 1
	else:
		print "Could not find the file you asked for."
		sys.exit
def GetFiles():
	CheckAndSetFolder(raw_input('FullPathtoTheFile--> ')) #give path to a file to test
	print "Checking folders in " + os.path.abspath(os.curdir)
	time.sleep(1)
	for dirname, dirnames, filenames in os.walk('.'):
		for filename in filenames:
			files.append( os.path.join(dirname, filename))
	print "Found these Files \n";

def CheckForDepricatedFiles():
	global xxyz
	for f in files:
		fileToCheck = f
		#print "Checking: " +fileToCheck
		for test in deprecatedFunctions:
			read = open(f, 'r').read();
			if test in read:
				xxyz=xxyz+1
				print "found " + test + " in " + fileToCheck


if __name__ == "__main__":
	
	xxyz = 0
	deprecatedFunctions = getCall()
	GetFiles() #get all individual files

	print"""
	==========
	"""


	CheckForDepricatedFiles()
	print "Found " +str(xxyz) +" depricated Functions"
