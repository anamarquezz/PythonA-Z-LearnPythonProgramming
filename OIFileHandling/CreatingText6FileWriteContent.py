#   FILE:
#       Attendence File
#
#   Instructions:
#   1.- Open File
#   2.- Read  And Search Content
#   3.- Close File
#
#       TYPES OF FILES:
#       > Text Files
#       > Binary Files

#   KNOW HOW
#   - Create A File
#   - Store Data
#   - Retrieve Data

#   CHARACTER            FUNCTION
#  |   r    |  -------  | Open file for reading only. Starts reading from beginning of file. This default mode. |
#  |   r*   |  -------  | Open file for reading and writing. File pointer placed at beginning of the file.      |
#  |   w    |  -------  | Open file for writing only. File pointer placed at beginning of the file. Overwrites. |
#  |                        existing file and creates a new one if it does not exists.                          |
#  |   w*   |  -------  | Same as w but also allows to read from file.                                          |
#  |   a    |  -------  | Open a file for appending Starts writting at the end of file. Creates                 |
#                            a new file if file does not exist.                                                 |

# open a file
# if is not passing any value it would be read as 'r' by default
fh = open("OIFileHandling/example.txt", "w")
fh.write("The tasks involved in file manipulation are reading data from file. \n")
fh.write("The tasks involved in file manipulation are reading data from file.")
fh.close()
