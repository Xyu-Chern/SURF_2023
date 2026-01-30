datasets={
    "id1":{
        "summary_prompt":["Define a function to return a sorted list of distinct characters obtained from a given string, after converting it to lowercase." ],     
        "test": "def check(candidate):\n    assert candidate(\"abcdecadeCADE\")==[\"a\", \"b\", \"c\", \"d\", \"e\"] \n    assert candidate(\"Jerry jERRY JeRRRY\")==[\" \",\"e\",\"j\", \"r\", \"y\" ]\n",
        "prompts": ["Assign the string \"{A}\" to a variable named \"my_string\".", "Lowercase the given string \"my_string\".", "Assign the distinct characters of the string to a variable named \"chars\".", "Sort these characters in alphabetical order.", "Print the resulting list of characters."],
        "mark":"True",
        "example":"input：\"abcdj\" \noutput： \"a\", \"b\", \"c\", \"d\", \"j\""
    },

    "id2":{
        "summary_prompt":["Define a function to return a list of formatted numbers, which are obtained by dividing each element of the given list of integers by their sum, multiplying by 100, and formatting them with a single decimal point."],
        "prompts": ["Define a list of integers named \"numbers\" with the values {numbers}.", "Calculate the sum of the elements in variable \"numbers\" and store the result to variable \"total\".", "Divide each element of the list by the total and multiply by 100, store the result to variable \"normalized\".", "Convert each element in variable \"normalized\" into a formatted string with single decimal point and store the result into \"formatted\".", "Print the variable \"formatted\"."],     
        "test": "def check(candidate):\n    assert candidate([56, 97, 19, 57, 69])==[\"18.8\", \"32.6\",\"6.4\", \"19.1\", \"23.2\"]\n    assert candidate([])==[]\n",
        "mark":"False",
        "example":"input:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] \noutput:[\"1.8\", \"3.6\", \"5.5\", \"7.3\", \"9.1\", \"10.9\", \"12.7\", \"14.5\", \"16.4\", \"18.2\"]"
    },

    "id3":{
        "summary_prompt":["Define a function to convert (hours , minutes) to seconds"],
        "prompts":["Writ,e a function that takes an integer minutes and converts it to seconds.", "Write a function that takes an integer hours and converts it to seconds.", "Print the total seconds of {a1} hours and {a2} minutes."],
        "test": "def check(candidate):\n    assert candidate(1,2) == 3720\n    assert candidate(32,32) ==117120 \n",
        "mark":"True",
        "example":"input:2,13 \noutput:7980"
    },

    "id4":{
        "summary_prompt":["Given a number to return the square of the corresponding Fibonacci number according to the given input value."],
        "prompts":["Implement a function which returns the n-th Fibonacci number.", "Implement a function that computes the square of an integer argument.", "Print out the square of {a1}-th Fibonacci number."],
        "test": "def check(candidate):\n    assert candidate([2]) == 1\n    assert candidate([3]) == 4\n",
        "mark":"True",
        "example":"input:[1] \noutput:1"
    },

    "id5":{
        "summary_prompt":["Given a list to return a max number compared with negatives and positives"],
        "prompts":["Assign the list of numbers \"{A}\" to a variable named \"my_numbers\".", "Count the number of negative numbers in the list as \"n_neg\".", "Count the number of positive numbers in the list as \"n_pos\".", "Print out the larger number of those two."],     
        "test": "def check(candidate):\n    assert candidate([-1,2,3,4])==3\n    assert candidate([-1,-2,,0,3,4])==2\n" ,
        "mark":"True",
        "example":"input:[1,2,3,4] \noutput:4"
    },

    "id6":{
        "summary_prompt":["Given four numbers to return a list of two means for first seconds and the elses "],
        "prompts":["Import the pandas library.", "Create a dataframe with a column labeled \"Yes\" with values [{a1}, {a2}] and a column named \"No\" with values [{a3}, {a4}].", "Compute the mean per column and store the value in a variable named means.", "Print the variable means."] ,     
        "test": "def check(candidate):\n    assert candidate(-10, 10, -20, 20)==[0.0, 0.0]\n    assert candidate(1,2,3,4)==[1.5, 3.5]\n",
        "mark":"True",
        "example":"input:50,21,131,2 \noutput:[35.5, 66.5]"
    },

    "id7":{
        "summary_prompt":[" Define a function that takes two parameters, namely the numbers a1 and a2. For a list of integers within a given range (from a3 to a4), it evaluates and returns the corresponding result based on the following conditions: if the number is a multiple of a1, it outputs \"fizz\"; If the number is a multiple of a2, output \"buzz\"; If the number is both a multiple of a1 and a multiple of a2, output \"fuzzbuzz\".,store all the results in a list named 'new_list' "],
        "prompts": ["Write a function that returns a number, for numbers multiple of {a1} print \"fizz\" instead of a number, for numbers multiple of {a2} print \"buzz\", for numbers which are multiples of both {a1} and {a2} \"fizzbuzz\".", "Create a list of integers ranging from {a3} to {a4}.", "Call the written function for each element in the list and store the result as \"new_list\".", "Print out the list \"new_list\"."] ,     
        "test": "def check(candidate):\n    assert candidate({\"a1\": 5, \"a2\": 3, \"a3\": 0, \"a4\": 9}) == [\"fizzbuzz\", 1, 2, \"buzz\", 4, \"fizz\", \"buzz\", 7, 8, \"buzz\"]\n    assert candidate({\"a1\": 9, \"a2\": 3, \"a3\": 0, \"a4\": 2}) == [\"fizzbuzz\", 1, 2]\n",
        "mark":"False",
        "example":"input:{\"a1\": 5,\"a2\": 3, \"a3\": 0, \"a4\": 9} \noutput:[\"fizzbuzz\", 1, 2, \"fizz\", 4]"
    },

    "id8":{
        "summary_prompt":[" Define a function to split the input string into words and return a binary list composed of adjacent words  "],
        "prompts":["Write a function that can take a string and return a list of word bigrams as pairs.", "Assign the string \"{a1}\" to a variable named sentence.", "Print out the bi-grams for the variable named sentence."],
        "test": "def check(candidate):\n    assert candidate(\"Have free hours and love children? Drive kids to school, soccer practice and other activities\") == [[\"Have\", \"free\"], [\"free\", \"hours\"], [\"hours\", \"and\"], [\"and\", \"love\"], [\"love\", \"children?\"], [\"children?\", \"Drive\"], [\"Drive\", \"kids\"], [\"kids\", \"to\"], [\"to\", \"school,\"], [\"school,\", \"soccer\"], [\"soccer\", \"practice\"], [\"practice\", \"and\"], [\"and\", \"other\"], [\"other\", \"activities.\"]]",
        "mark":"True",
        "example":"input:\"Have free\" \noutput:[\"Have\", \"free\"]"
    },

    "id9":{
        "summary_prompt":["Given the names [\"Kevin\", \"John\", \"Mike\", \"Mitch\"] as keys and corresponding notes [{a1}, {a2}, {a3}, {a4}] and find the key with the highest notes  "],
        "prompts": ["Assign the names [\"Kevin\", \"John\", \"Mike\", \"Mitch\"] as keys and corresponding notes [{a1}, {a2}, {a3}, {a4}] as values to a dictionary named \"my_notes\".", "Create a function that takes a dictionary of objects like {{ \"name\": \"John\", \"notes\": [3, 5, 4] }} and returns a dictionary of objects like {{ \"name\": \"John\", \"top_note\": 5 }}.", "For each name in the dictionary get the top_note and store the pairs of names and top_notes as \"my_list\".", "Find the name with the highest top_note and assign it to \"top_name\".", "Print the variable top_name."],
        "test": "def check(candidate):\n  assert candidate({\"a1\": [3, 5, 4], \"a2\": [3, 1, 1], \"a3\": [1, 2, 3], \"a4\": [0, 4, 4]}) == \"Kevin\"\n  ",
        "mark":"False",
        "example":"input:\"a1\": [1,2,3], \"a2\": [4,5,6], \"a3\": [8,8,8], \"a4\": [8,2,1] \noutput:\"Mike\""
    },

    "id10":{
        "summary_prompt":[" Given a hexadecimal number as input and returns its binary representation"],
        "prompts":["Create a function that will take a HEX number and returns the binary equivalent (as a string). E.g., to_binary(0xFF) = \"11111111\".", "Create a function that will take the output of the above function and return the HEX number. E.g., to_hex(\"11111111\") = 0xFF.", "Assign the value {a1} to a variable named \"my_hex\".", "Convert the variable \"my_hex\" into the binary equivalent as string named \"my_binary\".", "Convert \"my_binary\" back to a HEX number named \"result\".", "Print the result."],
        "test": "def check(candidate):\n    assert candidate(0xAA) == 170\n    assert candidate(0xAF) == 175",
        "mark":"True",
        "example":"input:0xFF \noutput:255"
    },

    "id11": {
        "example": "input:a1 = [\"a\", \"b\"], a2 = [1, 2], a3 = \"\" \noutput:False",
        "prompts": ["Assign the keys {a1} and values {a2} to a dictionary named \"my_dict\".", "Write a function \"invert\" that inverts the keys and values of a dictionary. E.g., invert({{ \"z\": \"q\", \"w\": \"f\" }}) = {{ \"q\": \"z\", \"f\": \"w\" }}.", "Write a function \"is_inverted\" that takes two dicts as arguments and returns a boolean which indicates if the second dict is an inversion of the first dict argument.", "Create a new variable \"my_dict2\" and initialize it with {a3} \"my_dict\".", "Print a boolean value indicating if \"my_dict2\" is the inverted dictionary of \"my_dict\"."],
        "summary_prompt":["Assign the keys {a1} and values {a2} to a dictionary named \"dic1\", initialize a new variable \"dic2\" with {a3} \"dic1\", check if \"dic2\" is the inverted(invert the keys and values) dictionary of \"dic1\"."],
        "test": "def check(candidate):\n    assert candidate(a1 = [\"a\", \"b\"], a2 = [1, 2], a3 = \"inverted\") == True\n    assert candidate(a1 = [\"a\", \"b\", \"c\"], a2 = [1, 2, -1], a3 = \"\") == False\n    assert candidate(a1 = [\"a\", \"b\", \"c\"], a2 = [1, 2, -1], a3 = \"inverted\") == True\n    assert candidate(a1 = [\"1\"], a2 = [1], a3 = \"\") == False\n",
        "mark":"False"
    },
    "id12": {
        "example": "input:a1 = \"David Jones\", a2 = 25, a3 = 175, a4 = 75, a5 = \"age\"  \noutput:25",
        "prompts": ["Defines class named \"Player\" that takes the following four arguments for a particular football player: name, age, height, weight.", "Also, create three functions for the class that returns the following strings: (1) get_age() returns \"{{name}} is age {{age}}\", (2) get_height() returns \"{{name}} is {{height}} cm\", (3) get_weight() returns \"{{name}} weighs {{weight}} kg\".", "Create an object named \"player\" with name \"{a1}\", age {a2}, height {a3}, weight {a4}.", "Call the getter for the {a5} of the player and return the result."],
        "summary_prompt":["Define a class that given name{a1}, age{a2}, height{a3}, weight{a4} of a player, output the attribute{a5} of the player in a number."],
        "test": "def check(candidate):\n    assert candidate(a1 = \"Paul Smith\", a2 = 50, a3 = 160, a4 = 60, a5 = \"weight\") == 60\n    assert candidate(a1 = \"Paul Smith\", a2 = 50, a3 = 160, a4 = 60, a5 = \"height\") == 160\n    assert candidate(a1 = \"Herr Schmidth Gold\", a2 = 50, a3 = 210, a4 = 60, a5 = \"height\") == 210\n    assert candidate(a1 = \"Paul Smith\", a2 = 5, a3 = 160, a4 = 60, a5 = \"age\") == 5\n",
        "mark": "True"
    },
    "id13": {
        "example": "input:[1, 2, 3, 12] \noutput:12",
        "prompts": ["Create a function \"num_len\" that takes a number num and returns its length. E.g., number_length(5000) = 4.", "Initialize a last \"my_list\" with the values {a1}", "return the longest number in this list."],
        "summary_prompt":["Define a function that given a list of numbers and return the longest number in this list."],
        "test": "def check(candidate):\n    assert candidate([-123, 2, 3, 12]) == -123\n    assert candidate([1]) == 1\n    assert candidate([-12, 1]) == -12\n    assert candidate([1, 22, 333, 4444, -55555]) == -55555\n",
        "mark": "True"
    },
    "id14": {
        "example": "input:1 \noutput:2",
        "prompts": ["Import the class LinearRegression from sklearn.", "Import math.", "Assign integers ranging from 0 to 10 (inclusive) to \"x\".", "Define a function \"f\" that multiplies a input argument by 2.", "Create a numpy array of numbers \"y\" by applying f to each element of x.", "Initialize a linear regression model.", "Fit the model to input x and output y (reshape both arguments with reshape(-1, 1)).", "Predict a variable \"x_hat\" at x=[[{a1}]] using the fitted model.", "Apply ceil() to the predicted value and print it as an integer."],
        "summary_prompt":["Given a number, print double of the number."],
        "test": "def check(candidate):\n    assert candidate(2) == 4\n    assert candidate(3) == 6\n    assert candidate(4) == 8\n    assert candidate(5) == 10\n",
        "mark": "False"
    },
    "id15": {
        "example": "input:\"hi\" \noutput:[\"hi\", \"jk\"]",
        "prompts": ["Create a function encrypt that takes a string as an argument and returns a string encrypted with the alphabet being rotated. The alphabet should be rotated in a manner such that the letters shift down by two places. For example: encrypt('hi') returns 'jk', encrypt('asdfghjkl') returns 'cufhijlmn', encrypt('gf') returns 'ih'.", "Create a function decrypt that decodes the encrypted string from encrypt() back into the original text.", "Assign \"{a1}\" to a variable named \"original_text\".", "Call the function encrypt with original_text as argument and assign the result to a variable named 'encrypted_text'.", "Call the function decrypt with encrypted_text as argument and assign the result to a variable named 'restored_text'.", "Create a list named \"my_result\" containing restored_text and encrypted_text as elements.", "Print the list."],
        "summary_prompt":["Given a string, shift down the all letters in the string by two places, output a list containing the original string and the new string."],
        "test": "def check(candidate):\n    assert candidate(\"asdfghjkl\") == [\"asdfghjkl\", \"cufhijlmn\"]\n    assert candidate(\"gf\") == [\"gf\", \"ih\"]\n    assert candidate(\"Hello World\") == [\"Hello World\", \"Hgnnq Wqtnf\"]\n    assert candidate(\"This is a LONG string for our encryption algOrithm.\") == [\"This is a LONG string for our encryption algOrithm.\", \"Tjku ku c LONG uvtkpi hqt qwt gpetarvkqp cniOtkvjo.\"]\n",
        "mark": "True"
    },
    "id16": {
        "example": "input:\"id\", \"1, 2, 2\", \"C\" \noutput:2",
        "prompts": ["Defines a class \"Person\" which takes name and id as constructor arguments.", "Extend the class with a function __hash__ which uses the {a1} property as hash value.", "Extend the class with a function __eq__ which returns true, if the hash value of the passed object and self are identical.", "Create a list \"persons\" with instances of Person and names \"Person A\", \"Person B\", \"Person {a3}\" and ids {a2}.", "Create a set \"unique_persons\" of this list.", "Print the number of elements in the set."],
        "summary_prompt":["Create a Python class called 'Person' with 'name' and 'id' attributes, add 'hash' and 'eq' methods to allow unique instances to be placed into a 'set', create a list named 'persons' containing three different 'Person' instances, use 'persons' to create a 'set' named 'unique_persons', and print the number of elements in 'unique_persons'."],
        "test": "def check(candidate):\n    assert candidate(\"name\", \"1, 2, 2\", \"C\") == 3\n    assert candidate(\"id\", \"2, 2, 2\", \"C\") == 1\n    assert candidate(\"id\", \"1, 2, 3\", \"C\") == 3\n    assert candidate(\"name\",  \"1, 1, 1\", \"B\") == 2\n",
        "mark": "True"
    },
    "id17": {
        "example": "input:29348 \noutput:[29348, \"29348\"]",
        "prompts": ["Python got drunk and the built-in functions str() and int() are acting odd: \n# str(4) = 4\n# str(\"4\") = 4\n# int(\"4\") = \"4\"\n# int(4) = \"4\".", "Create a function called int_to_str() that converts integers into strings. E.g., int_to_str(4) = \"4\".", "Create a function called str_to_int() that converts integers into strings. E.g., str_to_int(\"4\") = 4.", "Create a list named \"my_result\" with elements int_to_str({a1}) and str_to_int(\"{a1}\").", "Return the list."],
        "summary_prompt":["Define a function that given a number, return a list containing the original number and the string form of the number."],
        "test": "def check(candidate):\n    assert candidate(1) == [1, \"1\"]\n    assert candidate(123) == [123, \"123\"]\n    assert candidate(2344) == [2344, \"2344\"]\n    assert candidate(-1) == [-1, \"-1\"]\n",
        "mark": "True"
    },
    "id18": {
        "example": "input:\"Hello World\" \noutput:\"HELLO WORLD\"",
        "prompts": ["Initialize dictionary of Morse codes named 'chars_to_dots' with values ['A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.','G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..','M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.','S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-','Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----','1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....','6': '-....', '7': '--...', '8': '---..', '9': '----.','&': '.-...', \"'\": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-','-': '-....-', '+': '.-.-.', '\"': '.-..-.', '?': '..--..', '/': '-..-.']", "Create a function named 'encode_morse' that takes a string as an argument and returns the Morse code equivalent.", "Create a function named 'decode_morse' that takes a Morse code as an argument and returns the decodes string.", "Encode '{a1}' to morse code and assign the result to 'morse_code'.", "Decode the variable named 'morse_code' to a string named 'decoded_text'.", "Print the variable named 'decoded_text'."],
        "summary_prompt":["Given a string, first finds the Morse code equivalent, then decode the Morse code into a string(all caps), output the string."],
        "test": "def check(candidate):\n    assert candidate(\"Hello Foo\") == \"HELLO FOO\"\n    assert candidate(\"Hello WORLD\") == \"HELLO WORLD\"\n    assert candidate(\"foo BAR\") == \"FOO BAR\"\n    assert candidate(\"This is a long string\") == \"THIS IS A LONG STRING\"\n",
        "mark": "False"
    },
    "id19": {
        "example": "input:a1=\"[0,1,2,3]\", a2=4 \noutput:[1, 3]",
        "prompts": ["Initialize a list of integers with {a1} and a variable named target with a value of {a2}.", "Implement a function \"two_sum\" solving two sum problem given a list of integers and a target argument.", "Run the function and print out the result."],
        "summary_prompt":["Given an integer list{a1} and a target value{a2}, returns a list of two indices whose corresponding numbers add up to the target value."],
        "test": "def check(candidate):\n    assert candidate(a1=\"[1, 11, 111]\", a2=122) == [1, 2]\n    assert candidate(a1=\"[-1, 0, 2, 4]\", a2=3) == [0, 3]\n    assert candidate(a1=\"[10, 20, 30, 40]\", a2=70) == [2, 3]\n    assert candidate(a1=\"[-1, -1, 123, -123]\", a2=0) == [2, 3]\n",
        "mark": "True"
    },
    "id20": {
        "example": "input:10 \noutput:\"(-10, -10), (10, 10)\"",
        "prompts": ["Implement a function to sample n points from a bivariate normal distribution with mean (x_mean, y_mean) and standard deviation (x_std, y_std).", "Call the function to sample 100 points named points1 centered at ({a1}, {a1}) with standard deviation (1, 1).", "Call the function to sample 100 points named points2 centered at (-{a1}, -{a1}) with standard deviation (1, 1).", "Concatenate these data points.", "Implement the k-means clustering algorithm with n iterations and the centroids as return value.", "Run the algorithm on the points for 100 iterations with 2 clusters and assign the result to \"my_centroids\".", "Assign the centroid with negative coordinates to c1 and the one with positive coordinates to c2.Round the coordinates element-wise to the nearest integers and print the two centroids c1, c2 in the format of \"(x1, y1), (x2, y2)\"."],
        "summary_prompt":["Use bivariate normal distribution to sample 100 points named points1 with a mean of ({a1}, {a1}) and a standard deviation of (1, 1), and sample another 100 points named points2 with a mean of (-{a1}, -{a1}) and a standard deviation of (1, 1) using the same distribution. Concatenate these two sets of data points. Implement the k-means clustering algorithm with 100 iterations, using 2 clusters. Assign the centroid with negative coordinates to c1 and the one with positive coordinates to c2. Round each coordinate to the nearest integer and print the two centroids c1 and c2 in the format of \"(x1, y1), (x2, y2)\"."],
        "test": "def check(candidate):\n    assert candidate(20) == \"(-20, -20), (20, 20)\"\n    assert candidate(30) == \"(-30, -30), (30, 30)\"\n    assert candidate(40) == \"(-40, -40), (40, 40)\"\n    assert candidate(50) == \"(-50, -50), (50, 50)\"\n",
        "mark": "False"
    },
    "id21": {
        "example": "input:[1] \noutput:[0, 1]",
        "prompts": ["Define a list of integers named \"elements\" with values {numbers}.", "Calculate the sum of the even numbers of the list and store the result to variable \"even\".", "Calculate the sum of the odd numbers in the same list and store the result to \"odd\".", "Create a list named \"my_result\" containing the variables even and odd.", "Print the list."],
        "summary_prompt":["Calculate the sum of even numbers and the sum of odd numbers in a given list of integers. Return a list containing the sum of even numbers and the sum of odd numbers"],
        "test": "def check(candidate):\n    assert candidate([2e+100, 5e+100, -11, 10]) == [7e+100, -11]\n    assert candidate([]) == [0, 0]\n    assert candidate([-5, 1, 6, -25, -36, 6]) == [-24, -29]\n    assert candidate([73, 4, 14, 95, 69, 57, 82, 4, 75, 50, 91, 4, 83, 89, 61, 67, 53, 54, 48, 10]) == [270, 813]\n",
        "mark": "True"
    },
    "id22": {
        "example": "input:[\"a\", \"b\", \"c\", \"d\", \"e\", \"f\", \"g\"] \noutput:[\"a\", \"b\", \"c\", \"d\", \"e\", \"f\", \"g\"]",
        "prompts": ["Define a list named \"elements\" with the values {lst}.", "Count the number of zeros in variable elements and store the value into variable \"zero_count\".", "Scan through the list in order and remove all the zeros, store the result into variable \"non_zero\".", "Merge the variable non_zero and a new list containing \"zero_count\" 0s and store the result to \"result\". Print the variable \"result\"."],
        "summary_prompt":["Given a list, move all digits 0 to the end of the list and return the new list."],
        "test": "def check(candidate):\n    assert candidate([\"a\", 0, 0, \"b\", \"c\", \"d\", 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]) == [\"a\", \"b\", \"c\", \"d\", 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]\n    assert candidate([0]) == [0]\n    assert candidate([-1, 0, 1e-05, 0, 1e-30, 0]) == [-1, 1e-05, 1e-30, 0, 0, 0]\n    assert candidate([0, 1, null, 2, false, 1, 0]) == [1, null, 2, false, 1, 0, 0]\n",
        "mark": "True"
    },
    "id23": {
        "example": "input:{\"array\": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]，n_times=1000} \noutput:[3.8 7.3]",
        "prompts": ["Import numpy and initialize a numpy array named X with values {array}.", "Write a function that can take a numpy array and return an array of same size consisting of samples with replacement from the input.", "Call the function {n} times and stack the arrays into a new 2d array named \"samples\".", "Calculate the mean of each element in variable \"sample\" and store the result to \"mean\".", "Compute the 2.5 and 97.5 percentile of the variable mean and store the values into a new list named \"percentile\".", "return the variable \"percentile\"."],
        "summary_prompt":["Define a function that can return  the bootstrap 95% confidence interval of an array"],
        "test": "def check(candidate):\n    assert candidate({\"array\": \"consisting of 1000 randomly sampled integers ranging from 0 to 10\",  1000}) == [4.8025, 5.1975]\n    assert candidate({\"array\": \"consisting of 1000 randomly sampled integers ranging from 0 to 10\",  10000}) == [4.8025, 5.1975]\n    assert candidate({\"array\": \"consisting of 1000 uniformly sampled floats in [0, 1)\", \"n\": 1000}) == [0.4825, 0.5175]\n    assert candidate({\"array\": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], \"n\": 100}) == [1, 1]\n",
        "mark": "False"
    },
    "id24": {
        "example": "input:{\"a\": 8, \"b\": 2} \noutput:20",
        "prompts": ["Given two positive integers {a} and {b}, store the even single digits between a and b (inclusive) as \"my_digits\".", "Assign the sum of the even digits to the variable \"result\".", "Print the resulting number as integer."],
        "summary_prompt":["Given two positive integers {a} and {b}, return the sum of all even digits between a and b"],
        "test": "def check(candidate):\n    assert candidate({\"a\": 2, \"b\": 8}) == 20\n    assert candidate({\"a\": 2, \"b\": 6}) == 12\n",
        "mark": "True"
    },
    "id25": {
        "example": "input:[0, 4] \noutput:4",
        "prompts": ["Find the maximum element in the list {A} and assign it to variable \"my_max\".", "Find the minimum element in the same list.", "Compute the different between \"my_max\" and the minimum element.", "Print the difference"],
        "summary_prompt":["Given a list, return the difference between the maximum and minimum values in the list."],
        "test": "def check(candidate):\n    assert candidate([4, 0]) == 4\n    assert candidate([0]) == 0\n    assert candidate([0, 7, 6]) == 7\n    assert candidate([2, 4, 7, 20, 6]) == 18\n",
        "mark": "True"
    },
    "id26": {
        "example": "input:\"abcde\" \noutput:[\"a\", \"b\", \"c\", \"d\", \"e\"]",
        "prompts": ["Assign the string \"{A}\" to a variable named \"my_string\".", "Lowercase the given string \"my_string\".", "Assign the distinct characters of the string to a variable named \"chars\".", "Sort these characters in alphabetical order.", "Print the resulting list of characters."],
        "summary_prompt":["Given a string, sort the English letters in alphabetical order and return a list of non repeating lowercase letters"],
        "test": "def check(candidate):\n    assert candidate(\"abcdecadeCADE\") == [\"a\", \"b\", \"c\", \"d\", \"e\"]\n    assert candidate(\"aaaaAAAAaaaa\") == [\"a\"]\n    assert candidate(\"Jerry jERRY JeRRRY\") == [\" \", \"e\", \"j\", \"r\", \"y\"]\n    assert candidate(\"ddddc\") == [\"c\", \"d\"]\n",
        "mark": "True"
    },
    "id27": {
        "example": "input:{\"A\": \"abcde\", \"B\": \"ab\"} \noutput:\"abcde\"",
        "prompts": ["Create two variables \"a\" and \"b\" for the strings \"{A}\" and \"{B}\", respectively.", "Define a function \"len_str\" that returns the length of a string.", "Assign the length of each string to a seperate variable.", "Assign the longer string to the variable \"result\".", "Print the resulting string."],
        "summary_prompt":["Given two strings {A} and {B}, compare the lengths of the two strings and return the longer string."],
        "test": "def check(candidate):\n    assert candidate({\"A\": \"ab\", \"B\": \"abcde\"}) == \"abcde\"\n    assert candidate({\"A\": \"a\", \"B\": \"aa\"}) == \"aa\"\n    assert candidate({\"A\": \"aaaaaaaaaa\", \"B\": \"cdeee\"}) == \"aaaaaaaaaa\"\n    assert candidate({\"A\": \"f\", \"B\": \"gg\"}) == \"gg\"\n",
        "mark": "True"
    },
    "id28": {
        "example": "input:17.82 \noutput:99",
        "prompts": ["Assign the positive floating point number {A} to a variable \"f\".", "Compute the integer part of the number as variable \"a\".", "Assign the digits of the fractional part of the floating point number to an integer variable \"b\".", "Add them together and print the result."],
        "summary_prompt":["Given a float number, convert its decimal part of the number to an integer, and return the sum of it and the integer part of the float number."],
        "test": "def check(candidate):\n    assert candidate(1.1) == 2\n    assert candidate(1000000.0000001) == 1000001\n    assert candidate(0.0101) == 101\n    assert candidate(100.5) == 105\n",
        "mark": "True"
    },
    "id29": {
        "example": "input:\"CelebrAtion\" \noutput:5",
        "prompts": ["Assign the string value {s} to a variable \"my_string\".", "Lowercase the defined string.", "Count the number of vowels", "Print out the number"],
        "summary_prompt":["Given a string, return the number of vowels in it."],
        "test": "def check(candidate):\n    assert candidate(\"PaLm\") == 1\n    assert candidate(\"PrEdictiOn\") == 4\n    assert candidate(\"\") == 0\n    assert candidate(\"ABC\") == 1\n",
        "mark": "True"
    },
    "id30": {
        "example": "input:2 \noutput:2",
        "prompts": ["Assign the positive integer {n} to a variable \"f\".", "Create a list from 1 to \"f\" (inclusive).", "Create and initialize a variable named \"factorial\".", "Compute the product of all the values in the list and assign the product to \"factorial\".", "Print out the variable \"factorial\"."],
        "summary_prompt":["Given a positive integer, return its factorial."],
        "test": "def check(candidate):\n    assert candidate(4) == 24\n    assert candidate(10) == 3628800\n    assert candidate(1) == 1\n    assert candidate(5) == 120\n",
        "mark": "True"
    },
    "id31": {
        "example": "input:8,9 \noutput:(17,2)",
        "summary_prompt": [ "Enter 2 integer represent two edges of a triangle, calculate posible max and min length of its thired." ],
        "test": "def check(candidate):\n    assert candidate(5,7) == (11,3)\n    assert candidate(9,2) == (10,8)\n    assert candidate(1,1) == (1,1)\n    assert candidate(1000,1000) == (1999,1).",
        "prompts": [ "Given two positive integers, {a} {b}, which are the lengths of two edges of a triangle, compute the sum of the two edges and store it in a variable \"two-edges\". Compute the maximum length of the third edge by substracting 1 from \"two-edges\" and store the value in a variable \"maximum-edge\". Compute the minimum length of the third edge and store the value in a variable \"minimum-edge\". Assign value of maximum-edge and minimum-edge to a tuple named \"my_tuple\". Print the variable \"my_tuple\"." ],
        "mark": "True"
    },
    "id32": {
        "example": "input:2 \noutput:2",
        "summary_prompt": [ "Enter an integer and implement a function to compute and print out the remainder when dividing the factorial of {n} by 10." ],
        "test": "def check(candidate):\n    assert candidate(4) == 4\n    assert candidate(10) == 0\n    assert candidate(1) == 1\n    assert candidate(5) == 0",
        "prompts": [ "Compute factorial Implement a function to compute the remainder when dividing a number by 10. Print out the remainder when dividing the factorial of {n} by 10." ],
        "mark": "True"
    },
    "id33": {
        "example": "input:3 \noutput:3.14",
        "summary_prompt": [ "Given a positive integer, Compute the sum of internal angles in degrees for a regular polygon with n sides, convert the angle from degrees to radians, round to two decimal digits, print." ],
        "test": "def check(candidate):\n    assert candidate(4) == 6.28\n    assert candidate(1000) == 3135.31\n    assert candidate(10) == 25.13\n    assert candidate(100) == 307.88",
        "prompts": [ "Given a positive integer {n} and create a variable named \"n\" with this value. Compute the the total sum of internal angles in degrees of a regular-polygon with \"n\" sides. Convert the angle from degrees to radians. Round the angle to have two decimal digits. Print out the angle." ],
        "mark": "True"
    },
    "id34": {
        "example": "input:[\"111\",\"222\"] \noutput:333",
        "summary_prompt":[" Given a string array, convert two string to integers and compute the sum of them."],
        "test": "def check(candidate):\n    assert candidate([\"2\",\"4\"]) ==6\n    assert candidate([\"0\",\"12\"])==12\n    assert candidate([\"50\",\"100\"])==150\n    assert candidate([\"10000\",\"1\"]) ==10001",
        "prompts": [ "Assign two strings {s1} and {s2} to the variable named s1 and the variable named s2 respectively. Convert s1 and s2 to integers. Compute the sum of the two integers and store it as the variable s. Print out the variable s." ],
        "mark": "True"
    },
    "id35": {
        "example": "input:[4, 3, 8, 2] \noutput:35",
        "summary_prompt":" [Given an array, find its max and min value m1 and m2,then calcute the sum of a list from m1 to m2(inclusive).]",
        "test": "def check(candidate):\n    assert candidate([17, 16, 15, 10, 11, 12]) ==108\n    assert candidate([1,2]) ==3\n    assert candidate([10]) ==10\n    assert candidate([1,100]) ==5050",
        "prompts": [ "Initialize the variable named lst with an integer list {l}. Find the maximum of the variable lst and assign it to a variable named ma. Find the minimum of the variable lst and assign to a variable named mi. Create a list from mi and ma (inclusive). Print the sum of this list." ],
        "mark": "True"
    },
    "id36": {
        "example": "input:\"meaty\",\"apple\" \noutput:2",
        "summary_prompt":" [Given two string, calculate the number of vowels of the common characters of this two strings.]",
        "test": "def check(candidate):\n    assert candidate([\"fan\",\"forsook\"])==0\n    assert candidate([\"spout\",\"shout\"])==2\n assert candidate([\"happiness\",\"fitness\"])==2\n    assert candidate([\"code\",\"fork\"])==1 ",
        "prompts": [ "Implement a function to return the characters shared between two words. Implement a function to find the number of vowels in a string. Find the shared characters of {s1} and {s2}, concatenate them into a string, and assign it to a variable named s. Print the number of vowels in the variable s." ],
        "mark": "True"
    },
    "id37": {
            "example": "input:[-1, -2, 0, 1, 5] \noutput:-3",
            "summary_prompt": [ "Given an array,  find the negative numbers in it and print negative numbers' sum." ],
            "test": "def check(candidate):\n    assert candidate([5, 2, 0, 5, 10]) ==0\n    assert candidate([-100, -20, -3, 0, 0]) ==-123\n    assert candidate([-23, -2, -5, 1000, 23, -10, -100, -10]) ==-150\n    assert candidate([5, 1000, 0, 1, 0, 0, 0, 1, 1]) ==0",
            "prompts":["Given a list of integers {l}, assign the list to a varialbe named lst1. Find the negative numbers of the list and assign it to a new variable named lst2. Compute the sum of numbers in lst2. Print out the sum."],
            "mark": "True"
        },
    "id38": {
        "example": "input: {'a1': 'alco'}\noutput: 44369",
        "summary_prompt": ["Load from a file and print statistics."],
        "prompts": ["Import the pandas library.", "Read a dataframe \"df\" from the csv file located in \"./datasets/mlbootcamp5_train.csv\".", "Group by the column \"gender\" and assign the value counts for \"{a1}\" to a variable named \"my_counts\".", "Assign the attribute \"values\" of this variable and to a new variable named \"plain_list\".", "Print the maximum element of this list."],
        "test": "def check(candidate):\n    assert candidate('alco') == 44369",
        "mark": "True"
    },
    "id39": {
        "example": "input: {'s': 'Hello, World!'}\noutput: [5, 6]",
        "summary_prompt": ["Return a list of non-punctuation character lengths of a list of strings."],
        "prompts": ["Define a string named 's' with the value '{s}'.", "Import re and compile a regular expression that matches comma and period and store the result to variable 'pattern'", "Use the variable 'pattern' to substitute all the commas and periods in the string 's' and store the result to variable 's2'", "Split the string 's2' into a list of words with a space and store the result to variable 'words'", "Print a list of integers consisting of the length of each word in 'words'"],
        "test": "def check(candidate):\n    assert candidate('Hello, World!') == [5, 6]",
        "mark": "True"
    },
    "id40": {
        "example": "input: {'s': '#FFF'}\noutput: true",
        "summary_prompt": ["Convert a six hexadecimal digit string into list of RGB values."],
        "prompts": ["Create a variable named 's' with the value '{s}'.", "Lowercase the variable 's' and store the result to variable 's2'.", "Import re and compile a regular expression that matches a sharp symbol followed by three hexadecimal digits (0-9, a-f), store the result to variable 'pattern3'.", "Compile a regular expression that matches a sharp symbol followed by six hexadecimal digits (0-9, a-f), store the result to variable 'pattern6'.", "Print True if the variable 's2' if it matches with either of variables 'pattern3' or 'pattern6', False otherwise."],
        "test": "def check(candidate):\n    assert candidate('#FFF') == True",
        "mark": "True"
    },
    "id41": {
        "example": "input:[1, 1, 2, 2, 2, 2] \noutput:2",
        "prompts": ["Create a function called 'count_values' that takes a list of integers and returns a hash map of the number of times each integer appears in the list.", "Apply the function 'count_values' to the list '{lst}' and store the result to variable 'counts'.", "Print the integer with maximum count in the hash map 'counts', if the count is larger than half of the length of the list, otherwise print 'None'."],
        "summary_prompt":["Prints the number in a list of integers that occurs more than half the length of the list."],
        "test": "def check(candidate):\n    assert candidate({[]})==None\n    assert candidate({[100, 100, 0])==100\n    assert candidate([0, 0, 0, 0, 0, 1, 1, 1, 1])==0\n    assert candidate([1, 2, 3, 4, 5, 6, 6, 6, 6, 6])==None}",
        "mark":"True"
    },
    "id42": {
        "example": "input:{1}/{28}/{1990} \noutput:02/04/1990",
        "prompts": ["Import datetime and initialize a datetime object named 'today' with {month}/{day}/{year} (month/day/year).", "Add 7 days to the variable 'today' and store the result to variable 'week'.", "Print 'week' in the format '%m/%d/%Y'."], 
        "summary_prompt": ["According to the format of {month}/{day}/{year} (month/day/year), output the date seven days after the given date."],
        "test": "def check(candidate):\n    assert candidate({2}/{26}/{2000})==03/04/2000\n    assert candidate({12}/{28}/{2022})==01/04/2023\n    assert candidate({11}/{5}/{1274}})==11/12/1274\n    assert candidate({7}/{30}/{1600}})==08/06/1600}",
        "mark":"True"
    },
    "id43": {
        "example": "input:['apple', 'banana', 'carrot'] \noutput:True",
        "prompts": ["Create a function named 'word_weight' that takes a string as input and returns the sum of ASCII values of each alphabet in the string.", "Given a list of strings named 'words' with the value {words}', apply the function 'word_weight' to each word and store the result to variable 'weights'.", "Print 'True' if the sorted 'weights' is the same as the original 'weights', otherwise 'False'."],
        "summary_prompt": ["Computes the letter weight for each word in a list of strings, sorted by size, and checks whether the sorted list of weights is the same as the original list of weights."],
        "test": "def check(candidate):\n    assert candidate({'words': [\"I'll\", 'see', 'trees.']})==True\n    assert candidate({'words': ['a...', 'b?', 'c!', 'd']})==True\n    assert candidate({'words': ['', 'a', 'A']})==False\n    assert candidate({'words': ['ABC', 'ghijklmno', 'def']})==False\n}",
        "mark":"False"
    },
    "id44": {
        "example": "input:123456 \noutput:False",
        "prompts": ["Create a function named 'is_palindrome' that takes an integer as input and returns if the integer is a palindrome, by comparing stringified integer and its reversed string.", "Create a function named 'descent' that takes an integer as input and add each pair of adjacent digits together and return the result.", "Define an integer variable named 'base' with the value {n}.", "While the variable 'base' is not a single digit, apply the function 'is_palindrome' on 'base' and break if 'base' is palindrome. Otherwise, apply the function 'descent' to the variable 'base' and store the result to variable 'base'.", "Print 'False' if the variable 'base' is a single digit, otherwise print 'True'."],
        "summary_prompt": ["Checks whether an integer can be turned into a palindrome by repeatedly adding adjacent digits. Return True if it can, False if not."],
        "test": "def check(candidate):\n    assert candidate(1234)==False\n    assert candidate({123212)==True\n    assert candidate({11211230)==True\n    assert candidate({1112212124000131)==True}",
        "mark":"False"
    },
    "id45": {
        "example": "input:\"he@@l@hel@llo\" \noutput:\"helhelllo\"",
        "prompts": ["Define a string variable named 'input'.", "Iterating over variable 'input', if the current character is '@', remove this  character.","Print the rest of the characters"], 
        "summary_prompt": ["Remove all @ signs in the string."],
        "test": "def check(candidate):\n    assert candidate('@@@@')==\"\"\n    assert candidate('si@@@t boy')==\"sit boy\"\n    assert candidate('a@b@c@d@e@f@g@h@i@jkl')==\"abcdefghjkl\"\n    assert candidate('hello   @@world')==\"hello   world\"",
        "mark":"True"
    },
    "id46": {
        "example": "input:{80, 20} \noutput:100",
        "prompts":["Define a dictionary variable named 'input' with integers'.", "Iterating over variable 'input'and take out the integer inside.","Add up these integers"], 
        "summary_prompt": ["Extract and sum the integers in the dictionary."],
        "test": "def check(candidate):\n    assert candidate({50, 50})==100\n    assert candidate({20, 80})==100\n    assert candidate({10, 90})==100\n    assert candidate({90, 30})==120}",
        "mark":"True"
    },
    "id47": {
        "example": "input:[1, 3, 5, 7, 10] \noutput:29",
        "prompts": ["Create a variable named lst1 with value {l}", "Find the minimum and maximum of lst1 and assign them to variables a and b respectively", "Create a list from a to b (inclusive) and assign it to variable named lst2", "Find the elements that are in lst2 but not in lst1", "Print the sum of these elements"],
        "summary_prompt": ["Computes the sum of missing elements in a range of integer lists."],
        "test": "def check(candidate):\n    assert candidate([10, 7, 5, 3, 1])==29\n    assert candidate([10, 20, 30, 40, 50, 60])==1575\n    assert candidate([-100, 100])==0\n    assert candidate([-5, -10, 0, 10])==5}",
        "mark":"True"
    },
    "id48": {
        "example": "input:[\"1a\", \"a\", \"2b\", \"b\"] \noutput:[\"1a\", \"2b\"]",
        "prompts":["Initialize the variable named lst1 with a list {l}.", "Create a function called num_in_str() to check whether a string contains a number.", "Call the function num_in_str() to find strings in lst1 that have numbers and assign them to a list named lst2", "Print out lst2"],
        "summary_prompt": ["Check the elements inside a list whether a string contains a number. If there are, assign them to a list and print out it."],
        "test": "def check(candidate):\n    assert candidate(['abc', 'abc10'])==['abc10']\n    assert candidate({['abc', 'ab10c', 'a10bc', 'bcd'])==['ab10c', 'a10bc']\n    assert candidate(['this is a test', 'test1'])==['test1']\n    assert candidate(['t0t', '11', '0'])==['t0t', '11', '0']",
        "mark":"True"
    },
    "id49": {
        "example": "input:{2, 2, 2, 1} \noutput:8",
        "prompts": ["Define a function \"a\" that multiplies an integer argument by {a1} and returns the result.", "Define a function \"b\" that multiplies an integer argument by {a2} and returns the result.", "Define a function \"c\" that multiplies an integer argument by {a3} and returns the result.", "Create a list named \"abc\" which contains the three functions in order of definition.", "Assign the integer {a4} to a variable \"my_init\".", "Apply the first function of the list to \"my_init\" and name the result \"my_result\".", "For each subsequent function in the list, take the result of the previous function as input argument and assign the result to \"my_result\".", "Print the variable named \"my_result\"."],
        "summary_prompt": ["Multiply four numbers and output the result."],
        "test": "def check(candidate):\n    assert candidate({1, 1, 2, 1})==2\n    assert candidate(2, 2, 2, 2})==16\n    assert candidate({-2, 2, 2, 1})==-8\n    assert candidate({-2, -2, 2, 1})==8}",
        "mark":"True"
    },
    "id50": {
        "example": "input:{\"chair\", \"pencil\", \"arm\", \"arm\"} \noutput:True",
        "prompts": ["This function \"to_plural\" takes list of words in the singular form and returns a set of those words in the plural form adding an \"s\" to the end of the words, if they appear more than once in the list. E.g., pluralize([\"cow\", \"pig\", \"cow\", \"cow\"]) = {{\"cows\", \"pig\"}}, pluralize([\"table\", \"table\", \"table\"]) = {{\"tables\"}}.", "Create a function \"is_plural\" which returns True if the word passed as argument is in plural form.", "Assign {a1} to a variable named \"words\".", "Apply the function that returns plural forms to the variable \"words\" and name the result \"words_plural\".", "Define a boolean \"contains_plural\" and apply \"is_plural\" to each element of \"words_plural\" to detect if at least one word is in plural form.", "Print out whether or not \"words_plural\" contains a word in plural as boolean."],
        "summary_prompt": ["Determine whether the word in the dict is plural. Return True if it can, False if not."],
        "test": "def check(candidate):\n    assert candidate({\"arm\", \"arm\", \"arm\", \"arm\"})==True\n    assert candidate({\"chair\", \"arm\", \"pencil\", \"arm\"})==True\n    assert candidate({\"chair\", \"pencil\", \"arm\"})==False\n    assert candidate({\"chair\", \"pencil\", \"table\"})==False",
        "mark":"True"
    },
    "id51": {
        "example": "input: {'A': '[1,2,3,4]'}\noutput: 10",
        "summary_prompt": ["Compute the sum of prefix sums in a list."],
        "prompts": ["Assign the list of numbers {A} to a variable named my_relative_altitude.", "Compute the all prefix sum in the list (0 is the first element) and store as my_net_altitude.", "Find the largest number in the list my_net_altitude and store as max_altitude.", "Print out the variable max_altitude."],
        "test": "def check(candidate):\n    assert candidate([1,2,3,4]) == 10",
        "mark": "True"
    },
    "id52": {
        "example": "input: {'A': ['hello', 'world'], 'K': 1}\noutput: ['hello']",
        "summary_prompt": ["Truncate a sentence so that it contains k words."],
        "prompts": ["Assign the list of words {A} to a variable named my_sentences.", "Assign an integer {K} to a variable named k.", "Truncate the list such that it contains k words and store as truncated_list.", "Print out the variable truncated_list."],
        "test": "def check(candidate):\n    assert candidate(['hello', 'world'], 1) == ['hello']",
        "mark": "True"
    },
    "id53": {
        "example": "input: {'A': [1, 2, 2, 2]}\noutput: 1",
        "summary_prompt": ["Find the elements that appear one time in an array."],
        "prompts": ["Assign the list of integers {A} to a variable named my_numbers.", "Count the frequencies of the integers in my_numbers and store as frequency_table.", "Find the integer that has a frequency of 1 and store as one_time.", "Print out the variable one_time."],
        "test": "def check(candidate):\n    assert candidate([1, 2, 2, 2]) == 1",
        "mark": "True"
    },

    "id54": {
        "example": "input: {'A': [1, 2, 2, 2], 'Val': 2}\noutput: [1]",
        "summary_prompt": ["Remove all the occurrences of an element in an array."],
        "prompts": ["Assign the list of integers {A} to a variable named my_numbers.", "Assign an integer {Val} to a variable named val.", "Remove all occurrences of val in my_numbers and store the result as remove_numbers.", "Print out the variable remove_numbers."],
        "test": "def check(candidate):\n    assert candidate([1, 2, 2, 2], 2) == [1]",
        "mark": "True"
    },
    "id55": {
        "example": "input: {'A': [1, 2, 2, 2], 'Val': 2}\noutput: 'False'",
        "summary_prompt": ["Check whether the sum of an array is equal to a given value."],
        "prompts": ["Assign the list of integers {A} to a variable named my_numbers.", "Assign an integer {Val} to a variable named val.", "Sum all the numbers in my_numbers and store as sum_numbers.", "Check if sum_numbers is equal to val. If yes, return 'True', otherwise return 'False'."],
        "test": "def check(candidate):\n    assert candidate([1, 2, 2, 2], 2) == 'False'",
        "mark": "True"
    },
    "id56": {
        "example": "input: {'A': [1, 2, 2, 2], 'B': [3, 4]}\noutput: [1, 2, 2, 2, 3, 4]",
        "summary_prompt": ["Merge two sorted lists into one."],
        "prompts": ["Assign a sorted list {A} to a variable named my_numbers1.", "Assign a sorted list {B} to a variable named my_numbers2.", "Merge the two sorted lists into a new sorted list and store as new_list.", "Print the sorted new_list."],
        "test": "def check(candidate):\n    assert candidate([1, 2, 2, 2], [3, 4]) == [1, 2, 2, 2, 3, 4]",
        "mark": "True"
    },
    "id57": {
        "example": "input: {'A': [1], 'B': [5, 5, 5, 5, 5, 0]}\noutput: 1",
        "summary_prompt": ["Find the max contiguous subarray and return the sum."],
        "prompts": ["Assign the integer array {A} to a variable named my_array.", "Find the contiguous subarray of my_array with the largest sum and store as max_subarray.", "Compute the sum of max_subarray and store as sum_subarry.", "Print out the variable sum_subarray."],
        "test": "def check(candidate):\n    assert candidate([1]) == 1",
        "mark": "True"
    },
    "id58": {
        "example": "input: {'A': 1}\noutput: 1",
        "summary_prompt": ["Compute the largest integer not larger than the square root of a positive number."],
        "prompts": ["Assign the positive number {A} to a variable named my_number.", "Compute the square root of the number and store it as square_root.", "Compute the largest integer not larger than square_root and store it as largest_square_root.", "Print the integer largest_square_root."],
        "test": "def check(candidate):\n    assert candidate(1) == 1",
        "mark": "True"
    },
    "id59": {
        "example": "input: {'A': ['Hello', 'word']}\noutput: 'Hello'",
        "summary_prompt": ["Find the longest word in a word list."],
        "prompts": ["Assign the list of words {A} to a variable named my_words.", "Count the length of the words in the list and store as a dictionary word_count.", "Find the element with the largest count in dictionary word_count and store as longest_word.", "Print the variable longest_word."],
        "test": "def check(candidate):\n    assert candidate(['Hello', 'word']) == 'Hello'",
        "mark": "True"
    },
    "id60": {
        "example": "input: {'A': [1, 2, 3]}\noutput: 6",
        "summary_prompt": ["Sum all the unique numbers in a list."],
        "prompts": ["Assign the list of numbers {A} to a variable named my_numbers.", "Return the elements that appear exactly once in the list and store as my_uniques.", "Compute the sum of the list my_uniques and print it out."],
        "test": "def check(candidate):\n    assert candidate([1, 2, 3]) == 6",
        "mark": "True"
    },
    "id61": {
        "example": "input: {'A': [[3, 2], [2, 3]]}\noutput: 6",
        "summary_prompt": ["Compute the diagonal sum of a matrix."],
        "prompts": ["Assign the matrix {A} to a variable named my_matrix.", "Find the diagonal elements of my_matrix and store as diag_elements.", "Print out the sum of the variable diag_elements."],
        "test": "def check(candidate):\n    assert candidate([[3, 2], [2, 3]]) == 6",
        "mark": "True"
    },
    "id62": {
        "example": "input: {'A': [[3, 2], [2, 3]], 'B': [[3, 2], [2, 2]]}\noutput: 'False'",
        "summary_prompt": ["Compare two matrix determinants."],
        "prompts": ["Assign the matrix {A} to a variable named a.", "Assign the matrix {B} to a variable named b.", "Implement a function that computes the determinant of a matrix.", "Check whether the determinant of matrix a is larger than matrix b. If yes, print 'True', otherwise print 'False'."],
        "test": "def check(candidate):\n    assert candidate([[3, 2], [2, 3]], [[3, 2], [2, 2]]) == 'False'",
        "mark": "True"
    },
    "id63": {
        "example": "input: {'A': [[3, 2], [2, 3]], 'B': [[3, 2], [2, 3]]}\noutput: 10",
        "summary_prompt": ["Compute matrix multiplication sum of two matrices."],
        "prompts": ["Assign the matrix {A} to a variable named a.", "Assign the matrix {B} to a variable named b.", "Compute the multiplication of two matrices and store as result.", "Compute the sum of the result and print it out."],
        "test": "def check(candidate):\n    assert candidate([[3, 2], [2, 3]], [[3, 2], [2, 3]]) == 10",
        "mark": "True"
    },
    "id64": {
        "example": "input: {'A': [[3, 2], [2, 3]]}\noutput: 'True'",
        "summary_prompt": ["Check conditon number of a matrix is less than a threshold."],
        "prompts": ["Assign the matrix {A} to a variable named my_matrix.", "Assign the number {T} to a variable named t.", "Compute the condition number of my_matrix and store as result.", "Check whether the result is smaller than t. If yes, return 'True', otherwise return 'False'."],
        "test": "def check(candidate):\n    assert candidate([[3, 2], [2, 3]], 1) == 'True'",
        "mark": "True"
    },
    "id65": {
        "example": "input: {'A': [1, 3, 2, 2]}\noutput: 3.6265233750364456",
        "summary_prompt": ["Compute the log of sum exponential input."],
        "prompts": ["Assign the list of numbers {A} to a variable named my_numbers.", "Implement a function that computes the exponential output of a list.", "Implement a function that computes summation of a list.", "Implement a function that computes log of a number.", "Print out the log of sum exponential my_numbers."],
        "test": "def check(candidate):\n    assert abs(candidate([1, 3, 2, 2]) - 3.6265233750364456) < 1e-6",
        "mark": "True"
    },

    "id66": {
        "example": "input: {'A': [[1, 3], [2, 2]], 'K': 1}\noutput: [[2, 2]]",
        "summary_prompt": ["Find the k nearest points to the origin."],
        "prompts": ["Assign the list of points {A} to a variable named my_points.", "Assign the integer {K} to a variable named k.", "Implement a function that computes the distance between a point and the origin (0,0).", "Implement a function that computes the k closest points in an array to the origin and store as result.", "Compute the k closest points in my_points and print them out."],
        "test": "def check(candidate):\n    assert candidate([[1, 3], [2, 2]], 1) == [[2, 2]]",
        "mark": "True"
    },
    "id67": {
        "example": "input: {'s1': 'Geeks for Geeks', 's2': 'Learning from Geeks for Geeks'}\noutput: ['Learning', 'from']",
        "summary_prompt": ["Find uncommon words in two sentences."],
        "prompts": ["Assign a sentence '{s1}' to a variable named sentence1.", "Assign a sentence '{s2}' to a variable named sentence2.", "Split sentence1 into words and assign them to words1.", "Split sentence2 into words and assign them to words2.", "Find the words that appear once in both words1 and words2 and assign them to uncommon_words.", "Print uncommon_words."],
        "test": "def check(candidate):\n    assert candidate('Geeks for Geeks', 'Learning from Geeks for Geeks') == ['Learning', 'from']",
        "mark": "True"
    },
    "id68": {
        "example": "input: {'lst1': [2, 3, 1, 2, 3]}\noutput: [2, 3]",
        "summary_prompt": ["Find duplicates in a list."],
        "prompts": ["Initialize a variable named lst1 with a list {lst1}.", "Create a frequency table of elements in lst1.", "Find the elements with frequency larger than 1 and assign them to a list lst2.", "Print out lst2."],
        "test": "def check(candidate):\n    assert candidate([2, 3, 1, 2, 3]) == [2, 3]",
        "mark": "True"
    },
    "id69": {
        "example": "input: {'w': 'popular'}\noutput: 1",
        "summary_prompt": ["Find the first non-repeating character in a string."],
        "prompts": ["Assign a string '{w}' to a variable named w1.", "Get the first non-repeating character in w1.", "Find its corresponding index and assign it to n1.", "Print out n1."],
        "test": "def check(candidate):\n    assert candidate('popular') == 1",
        "mark": "True"
    },
    "id70": {
        "example": "input: {'s1': 'Geeks for Geeks', 's2': 'Learning from Geeks for Geeks'}\noutput: ['Learning', 'from']",
        "summary_prompt": ["Find uncommon words in two sentences."],
        "prompts": ["Assign a sentence '{s1}' to a variable named sentence1.", "Assign a sentence '{s2}' to a variable named sentence2.", "Split sentence1 into words and assign them to words1.", "Split sentence2 into words and assign them to words2.", "Find the words that appear once in both words1 and words2 and assign them to uncommon_words.", "Print uncommon_words."],
        "test": "def check(candidate):\n    assert candidate('Geeks for Geeks', 'Learning from Geeks for Geeks') == ['Learning', 'from']",
        "mark": "True"
    },

    "id71": {
        "example": "input: {'s1': 'Hi all, my name is Tom...I am originally from Australia.'}\noutput: 4.5",
        "summary_prompt": ["Compute the average word length of a sentence."],
        "prompts": ["Assign a sentence '{s1}' to a variable named sentence1.", "Split sentence1 into words and assign them to words1.", "Remove punctuation in words1.", "Compute the average word length in words1 and assign it avg.", "Print avg."],
        "test": "def check(candidate):\n    assert math.isclose(candidate('Hi all, my name is Tom...I am originally from Australia.'), 4.5, rel_tol=1e-9, abs_tol=0.0)",
        "mark": "True"
    },
    "id72": {
        "example": "input: {'w1': 'find', 'w2': 'ding'}\noutput: false",
        "summary_prompt": ["Compare the character frequencies in two strings."],
        "prompts": ["Assigns strings {w1} and {w2} to variables w1 and w2 respectively", "Lower-case w1 and w2", "Count the frequency of letters in w1 and w2 and assign them to f1 and f2", "Print if f1 is equal to f2"],
        "test": "def check(candidate):\n    assert candidate('find', 'ding') == False",
        "mark": "True"
    },
    "id73": {
        "example": "input:\"abc\" \noutput:\"cba\"",
        "summary_prompt":" [ Enter a string and output it in reverse order ]",
        "test": "def check(candidate):\n    assert candidate(\"ape\")==\"epa\"\n    assert candidate(\"geeksforgeeks\")==\"skeegrofskeeg\"\n    assert candidate(\"apple\")==\"elppa\"\n    assert candidate(\"april\")==\"lirpa\"",
        "prompts": [ "Assign a string {w} to a variable named w1. Concatenate the elements in w1 from end to beginning and assign it to w2. Print w2." ],
        "mark": "True"
    },
    "id74": {
        "example": "input: {'n': 12}\noutput: -5434",
        "summary_prompt": ["Calculate the difference between the squared sum and the sum of squares."],
        "prompts": ["Assign a natural number {n} to named num", "Create a list from 1 to num and assign it to a variable lst1", "Compute the sum of squared of the numbers in lst1 and assign n1", "Compute the sum of the numbers in lst1 and assign its square to n2", "Print out the difference between n1 and n2"],
        "test": "def check(candidate):\n    assert candidate(12) == -5434",
        "mark": "True"
    },
    "id75": {
        "example": "input: {'lst1': [0.3, 1.0, 2.0], 'lst2': [1.0, 2.0, 3.0]}\noutput: 0.9832301408945487",
        "summary_prompt": ["Compute the cosine similarity between two vectors."],
        "prompts": ["Assigns a list {lst1} to a variable named vec1", "Assigns a list {lst2} to a variable named vec2", "Normalize vec1", "Normalize vec2", "Compute the dot product of vec1 and vec2", "Print out the dot product"],
        "test": "def check(candidate):\n    assert math.isclose(candidate([0.3, 1.0, 2.0], [1.0, 2.0, 3.0]), 0.9832301408945487, rel_tol=1e-9, abs_tol=0.0)",
        "mark": "True"
    },
    "id76": {
        "example": "input: {'lst1': [0.0, 0.0, 0.0], 'lst2': [1.0, 2.0, 3.0], 'lst3': [0.1, 0.2, 0.3]}\noutput: true",
        "summary_prompt": ["Compare vector distances to the origin."],
        "prompts": ["Assigns a list {lst1} to a variable named vec1", "Assigns a list {lst2} to a variable named vec2", "Assigns a list {lst3} to a variable named vec3", "Convert vec1, vec2, and vec3 to numpy array", "Implement a function called dist() to compute the distance between two vectors", "Compute the distance between vec1 and vec2 and assign it to d1", "Compute the distance between vec1 and vec3 and assign it to d2", "Print out whether d1 is larger than d2"],
        "test": "def check(candidate):\n    assert candidate([0.0, 0.0, 0.0], [1.0, 2.0, 3.0], [0.1, 0.2, 0.3]) == True",
        "mark": "True"
    },

    "id77": {
        "example": "input: {'l1': [1, 1, 1, 1, 1], 'l2': [1, 2, 3, 4, 5]}\noutput: 0.0",
        "summary_prompt": ["Find the smaller standard deviation given two lists."],
        "prompts": ["Initialize a variable named lst1 with a list {l1}.", "Initialize a variable named lst2 with a list {l2}.", "Create a function called std() to compute the standard deviation given a list of numbers.", "Call the function std() to calculate standard deviations for lst1 and lst2.", "Print out the smaller standard deviation."],
        "test": "def check(candidate):\n    assert math.isclose(candidate([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]), 0.0, rel_tol=1e-9, abs_tol=0.0)",
        "mark": "True"
    },
    "id78": {
        "example": "input: {'l1': [1, 1, 1, 1, 1], 'l2': [1, 2, 3, 4, 5]}\noutput: 1.0",
        "summary_prompt": ["Find the smaller mean given two lists."],
        "prompts": ["Initialize a variable named lst1 with a list {l1}.", "Initialize a variable named lst2 with a list {l2}.", "Create a function called mean() to compute the mean given a list of numbers.", "Call the function mean() to calculate means for lst1 and lst2.", "Print out the smaller mean."],
        "test": "def check(candidate):\n    assert math.isclose(candidate([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]), 1.0, rel_tol=1e-9, abs_tol=0.0)",
        "mark": "True"
    },
    "id79": {
        "example": "input: {'l1': [1, 1, 1, 1, 1]}\noutput: 0.0",
        "summary_prompt": ["Compute coefficient of variation given a list."],
        "prompts": ["Initialize a variable named lst1 with a list {l1}.", "Compute the mean and the standard deviation for lst1 and assign it variable avg and sd, respectively", "Compute the coeffeicient of variation", "Print out the coefficient of variation"],
        "test": "def check(candidate):\n    assert math.isclose(candidate([1, 1, 1, 1, 1]), 0.0, rel_tol=1e-9, abs_tol=0.0)",
        "mark": "True"
    },
    "id80": {
        "example": "input:[0,0] \noutput:0",
        "summary_prompt":" [ Given a list, calculate the sum of the its absolute value ]",
        "test": "def check(candidate):\n    assert candidate([1,1])==2\n    assert candidate([-1, 1, -100, 100])==202\n    assert candidate([0, 0, 59, 1, 40])==100\n    assert candidate([-50, -10, 40, 200, 1000])==1300",
        "prompts": [ "Initialize a variable named lst1 with a list {l1}. Get the absolute value of every element in lst1 and assign to a lst2, Compute the sum of lst2 and assign to l1, Print out l1." ],
        "mark": "True"
    },
    "id81": {
        "example": "input:{\"lst1\": [0.3, 1.0, 2.0, -2.0, 4.0, -5.0]}\noutput: 0.017307532290566904",
        "summary_prompt": ["Compute z-statistic given a list."],
        "prompts": ["Assigns a list {lst1} to a variable named lst1", "Compute the sample mean of lst1", "Compute the sample standard deviation of lst1", "Compute the z-statistic to test whether its mean is 0", "Return the z-statistic."],
        "test": "def check(candidate):\n    assert candidate([0.3, 1.0, 2.0, -2.0, 4.0, -5.0]) == 0.017307532290566904\n    assert candidate([1.3, 5.0, 2.1, -2.4, 4.1, 5.1]) == 0.9670745372626464\n    assert candidate([1.3, 15.0, 2.9]) == 1.046418644730305\n    assert candidate([0.3, -1.0, -2.0, 5.0, 1.0, 5.1]) == 0.5092873663524808\n    assert candidate([10.3, 12.0, 20.0, 21.0, 40.0, 5.0, 10.0, 20.0, 23.0, 15.0]) == 1.8989720877738328",
        "mark": "True"
    },

    "id82": {
        "example": "input:{\"lst\": [3, -3, 2, -2]}\noutput: [3, 2, -3, -2]",
        "summary_prompt": ["Move all negative elements in a list to the end."],
        "prompts": ["Assign a list {lst} to named lst1", "Separate lst1 into two lists, lst_pos and lst_neg which contain all the positive numbers and all the negative numbers repsectively", "Concatenate lst_pos and lst_neg and assign it lst2", "Return lst2."],
        "test": "def check(candidate):\n    assert candidate([3, -3, 2, -2]) == [3, 2, -3, -2]\n    assert candidate([-5, 7, -3, -4, 9, 10, -1, 11]) == [7, 9, 10, 11, -5, -3, -4, -1]\n    assert candidate([-1000, 11]) == [11, -1000]\n    assert candidate([9, -10, 8, 2, -77, -50, 11, 6]) == [9, 8, 2, 11, 6, -10, -77, -50]\n    assert candidate([-50, -70, -30, 4, 3, -100, 1]) == [4, 3, 1, -50, -70, -30, -100]",
        "mark": "True"
    },
    "id83": {
        "example": "input:\"2a4b\" \noutput:24",
        "summary_prompt": [ "Initialize a variable with a string, convert to lowercase, remove alphabetical characters then print" ],
        "test": "def check(candidate):\n    assert candidate(\"br2ace\")==2\n    assert candidate(\"100\")==100\n    assert candidate(\"3g4lc\")==34\n    assert candidate(\"12Apple0\")==120",
        "prompts":[ "Initialize a variable named w with a string {w}. Lower every character in w. Replace every alphabetical characters in w with ''. Print out the new word after substitution." ],
        "mark": "True"
    },
    "id84": {
        "example": "input: [[0.884, 0.209], [0.067, 0.381], [0.503, 0.821], [0.306, 0.592], [0.417, 0.519]] \noutput: 0.6399499999999999",
        "summary_prompt": ["Find the largest norm among n-dimensional points."],
        "prompts": ["Import and initialize a numpy array \"X\" with the values {X}.", "Calculate the dot product between all rows and store the result to \"Xn\", where (i, j) element stores the dot product between i-th and j-th  row of \"X\".", "Set the diagonal elements of \"Xn\" to 0.", "Return the maximum value (cast as a float) in \"Xn\"."],
        "test": "def check(candidate):\n    assert candidate([[0.884, 0.209], [0.067, 0.381], [0.503, 0.821], [0.306, 0.592], [0.417, 0.519]]) == 0.6399499999999999\n    assert candidate([[2, 2], [1, 0], [0, 4], [2, 4], [1, 1], [0, 3], [1, 0], [1, 0], [1, 3], [0, 1]]) ==16\n    assert candidate([[1, 0, 3], [4, 3, 4], [4, 1, 2], [0, 1, 0], [3, 3, 2]]) ==29\n    assert candidate([[1.022,-0.668],[-1.082,0.063],[-0.181,0.841],[0.891,1.533],[1.195,-1.69]]) ==2.35021\n    assert candidate([[-8,2,-3],[2,-10,-5],[-5,5,-8],[-3,2,-2],[3,6,2]]) ==74",
        "mark":"True"
    },

    "id85": {
        "example": "input: pred: [1, 1, 1, 1, 1, 0, 1, 0, 0, 0], y: [0, 1, 1, 0, 1, 0, 0, 0, 0, 1] \noutput: 0.6",
        "summary_prompt": ["Given two arrays (pred, gold), calculate the F1 score."],
        "prompts": ["Initialize numpy arrays \"pred\" with the values {pred}, \"y\" with the values {y}.", "Compare the equivalence of two arrays and store the results as \"match\".", "Assign the boolean array for whether \"y\" is greater than 0 to a variable \"non_zero\".", "Perform the logical \"AND\" operation between \"match\" and \"non_zero\", store the result as \"correct\".", "Compute the precision by dividing the number of True values in \"correct\" by that in \"pred\", and store as \"prec\".", "Compute the recall by dividing the number of True values in \"correct\" by the number of actual non-zero values in \"y\", and store the result as \"rec\".", "Calculate the harmonic mean between \"prec\" and \"rec\", return the value."],
        "test": "def check(candidate):\n    assert candidate([1, 1, 1, 1, 1, 0, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 1]) == 0.6\n    assert candidate([0, 1], [1]) == None\n    assert candidate([0], [1]) == None\n    assert candidate([2], [2]) == None",
        "mark": "True"
    },

    "id86": {
        "example": "input: ACapitalLetterWords \noutput: A Capital Letter Words",
        "summary_prompt": ["Add spaces before capital letters."],
        "prompts": ["Initialize a string named \"concat\" with {x}.", "Import the regex module and define a pattern \"pat\" that matches capital alphabets that can be referenced as a group.", "Find all the matches in \"concat\" with \"pat\", and insert an additional whitespace before the matched character with then store the result to \"result\".", "Return \"result\"."],
        "test": "def check(candidate):\n    assert candidate('ACapitalLetterWords') == ' A Capital Letter Words'\n    assert candidate('camelCaseMethod') == 'camel Case Method'\n    assert candidate('ABCDE') == ' A B C D E'\n    assert candidate('splitDB') == 'split D B'",
        "mark": "True"
    },
    "id87": {
        "example": "input: [0, 0, 0, 0, 100] \noutput: [100]",
        "summary_prompt": ["Remove data points in the tail (2sigma) of normal distribution."],
        "prompts": ["Initialize a list \"x\" with the values {x}.", "Assuming the normal distribution, calculate mean and standard deviation of \"x\" using numpy and store the results to \"mean\" and \"std\".", "Find the values in x that are either smaller than mean - std * std or larger than mean + std * std and store the results to \"results\".", "Sort \"results\" in ascending order and return it."],
        "test": "def check(candidate):\n    assert candidate([0]) == []\n    assert candidate([100]) == [100]\n    assert candidate([10000000000000000000000000000000000000000000000000]) == [10000000000000000000000000000000000000000000000000]\n    assert candidate([-100]) == [-100]",
        "mark": "True"
    },

    "id88": {
        "example": "input:{\"x\": [4, 2, 3, 1, 0, 3, 3, 3, 2, 1]}\noutput: [[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0], [0, 1, 0, 0, 0]]",
        "summary_prompt": ["Convert values into categorical variables."],
        "prompts": ["Initialize a list \"x\" with the values {x}\nObtain a list of unique elements in x and sort them, store the results to \"vocab\".\nCreate a hash map from the values of \"vocab\" to their indices and store the result to \"v2i\".\nInitialize a numpy array of zeros named \"features\" whose row size is the length of x and column size is the length of \"index\", with a data type of int.\nFor each element in x, assign 1 to (i, j) location of features, where i is the index of the current element and j is the mapped value of the current element using \"v2i\".\nReturn \"features\"."],
        "test": "def check(candidate):\n    assert candidate([4, 2, 3, 1, 0, 3, 3, 3, 2, 1]) == [[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0], [0, 1, 0, 0, 0]]\n    assert candidate([0, 1, 2]) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]\n    assert candidate([1, 1, 1, 1, 1]) == [[1], [1], [1], [1], [1]]\n    assert candidate([0, 0, 0, 0, 0]) == [[1], [1], [1], [1], [1]]\n    assert candidate([0, 0, 1, 1]) == [[1, 0], [1, 0], [0, 1], [0, 1]]",
        "mark": "True"
    },

    "id89": {
        "example": "input:{\"fun\": \"len\", \"x\": [\"a\", \"b\", \"c\"]}\noutput: {\"1\": [\"a\", \"b\", \"c\"]}",
        "summary_prompt": ["Group items in an array using a provided function."],
        "prompts": ["Initialize a variable \"x\" with {x}", "Apply the function \"{fun}\" to each element in the list and store the results to \"mapped\".", "Convert each element in \"mapped\" into string.", "Define \"results\" with a dictionary whose keys are the unique values in \"mapped\" and values are empty lists.", "Looping over the zip of \"mapped\" and \"x\", append the value in \"x\" to the value of \"results\" using the value in \"mapped\" as the key.", "Return \"results\"."],
        "test": "def check(candidate):\n    assert candidate([\"a\", \"b\", \"c\"], \"len\") == {\"1\": [\"a\", \"b\", \"c\"]}\n    assert candidate([\"apple\", \"banana\", \"orange\", \"peach\"], \"len\") == {\"5\": [\"apple\", \"peach\"], \"6\": [\"banana\", \"orange\"]}\n    assert candidate([1, 2, 3, \"a\", \"b\", \"c\"], \"type\") == {\"int\": [1, 2, 3], \"str\": [\"a\", \"b\", \"c\"]}\n    assert candidate([[1, 2, 3], \"a\", \"b\", \"c\"], \"len\") == {\"1\": [\"a\", \"b\", \"c\"], \"3\": [[1, 2, 3]]}\n    assert candidate([1, 2, 3, \"1\", \"2\", \"3\"], \"str\") == {\"2\": [2, \"2\"], \"3\": [3, \"3\"], \"1\": [1, \"1\"]}",
        "mark": "True"
    },
    "id90": {
        "example": "input:{\"array\": [1, 2, 3, 4, 5]}\noutput: 4",
        "summary_prompt": ["Given an array of \"prices\", find the max profit."],
        "prompts": ["Initialize a variable \"best\" with -1, \"array\" with {array}", "Assign the first element of \"array\" to a variable named \"minimum\".", "In a for loop over \"array\" starting from the second element, do 1) update \"best\" when the element minus \"minimum\" is larger than \"best\", and 2) update \"minimum\" with the value of the element if it is smaller than \"minimum\".", "Return \"best\"."],
        "test": "def check(candidate):\n    assert candidate([1, 2, 3, 4, 5]) == 4\n    assert candidate([5, 2, 3, 4, 0]) == 2\n    assert candidate([12, 7, 8, 5, 9, 5, 14, 9, 8, 9]) == 9\n    assert candidate([1, 10, 1, 10, 0]) == 9\n    assert candidate([1, 2, 3, 2, 1]) == 2",
        "mark": "True"
    },
    "id91": {
        "example": "input:{\"target\": 1, \"nums\": [1, 2, 1, 2, 1]}\noutput: 6",
        "summary_prompt": ["Sum of all position indices where a value appears."],
        "prompts": ["Initialize a variable \"target\" with {target}, and \"nums\" with {nums}, and \"result\" with an empty list.", "Enumerating over \"nums\", compare each element with \"target\" and add its index position to \"result\" if they are equivalent.", "Return the sum of elements in \"result\"."],
        "test": "def check(candidate):\n    assert candidate(1, [1, 2, 1, 2, 1]) == 6\n    assert candidate(1, [0, 0, 0]) == 0\n    assert candidate(1, [1.1, 2, 3, 2, 1]) == 4\n    assert candidate(\"1\", [1, 2, 3, 2, 1]) == 0\n    assert candidate(\"1\", [1, \"1\", 2, \"1\"]) == 4",
        "mark": "True"
    },
    "id92": {
        "example": "input:{\"nums\": [1, 3, 4], \"N\": 4}\noutput: 2",
        "summary_prompt": ["Find a missing number given a list and a max number."],
        "prompts": ["Initialize a variable \"nums\" with {nums} and a variable \"N\" with {N}.", "Initialize a variable \"all_nums\" which is a set of numbers between 1 and N.", "Subtract the set of numbers in \"nums\" from \"all_nums\", and store the result to \"diff\".", "Pop the only element in \"diff\" and return it."],
        "test": "def check(candidate):\n    assert candidate([1, 3, 4], 4) == 2\n    assert candidate([1, 2, 3, 4], 5) == 5\n    assert candidate([4, 3, 9, 7, 8, 5, 2, 1, 10], 10) == 6\n    assert candidate([6, 15, 13, 2, 14, 17, 7, 16, 11, 9, 3, 10, 8, 5, 12, 1, 20, 4, 19], 20) == 18\n    assert candidate([], 1) == 1",
        "mark": "True"
    },
    "id93": {
        "example": "input:{\"x\": [[1, 2, 3, 4, 5], [0, 1, 3, 5, 7], [0, 2, 3, 4, 5]]}\noutput: [1, 2, 3, 4, 5]",
        "summary_prompt": ["Common numbers among rows in a matrix."],
        "prompts": ["Assign {x} to a variable named \"X\".", "Initialize a variable named \"common\" with a set of unique elements in the first index of \"X\".", "Iterating over \"X\", update \"common\" with an intersection of \"common\" and the set of unique elements in the current index of \"X\".", "Return \"common\" as a list."],
        "test": "def check(candidate):\n    assert candidate([[1, 2, 3, 4, 5], [0, 1, 3, 5, 7], [0, 2, 3, 4, 5]]) == [1, 2, 3, 4, 5]\n    assert candidate([[1, 1], [1, 1]]) == [1]\n    assert candidate([[1, 2, 3], [2, 3, 4], [3, 4, 5]]) == [3]\n    assert candidate([[1, 12, 56, 21, 5], [21, 2, 6, 11, 7], [5, 7, 13, 8, 21], [5, 21, -5, 6, 8]]) == [21]\n    assert candidate([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]) == [1, 2, 3, 4, 5]",
        "mark": "True"
    },
    "id94": {
        "example": "input:{\"start\": 1}\noutput: 1",
        "summary_prompt": ["Obtain the sum of Collatz sequence starting from a given number."],
        "prompts": ["Initialize a variable \"start\" with {start}, and \"seq\" with a list containing {start}.", "While the value is not 1, perform the following: if \"start\" is an even number, divide by 2, otherwise multiply by 3 and add 1, then store the number to \"start\" as well as appending to \"seq\".", "Return the sum of all numbers in \"seq\"."],
        "test": "def check(candidate):\n    assert candidate(1) == 1\n    assert candidate(9) == 55\n    assert candidate(27) == 101440\n    assert candidate(28) == 330\n    assert candidate(123456789) == 1266590663",
        "mark": "True"
    },
    "id95": {
        "example": "input: {'start': 'A', 'swap': ['AB', 'BC', 'CA', 'BC', 'AC']} \noutput: C",
        "summary_prompt": ["Name the location of a \"ball\" after cup swapping."],
        "prompts": ["Define a variable \"pos\" with \"{start}\", \"swap\" with {swap}.", "Write a function \"move\" that takes two strings x and y as input, and replace any appearance of x in y with an empty string, then return y.", "For each element in \"swap\", if it contains \"pos\", call \"move\" on \"pos\" and the current element and store the result to \"pos\".", "Return \"pos\"."],
        "test": "def check(candidate):\n    assert candidate({'start': 'A', 'swap': ['AB', 'BC', 'CA', 'BC', 'AC']}) == 'C'\n    assert candidate({'start': 'B', 'swap': ['AC', 'CA']}) == 'B'\n    assert candidate({'start': 'C', 'swap': ['AB', 'BC', 'CA', 'BC', 'AC', 'AB', 'CA', 'BC', 'AC', 'BA']}) == 'B'\n    assert candidate({'start': 'C', 'swap': ['AB', 'AC']}) == 'A'\n    assert candidate({'start': 'A', 'swap': []}) == 'A'",
        "mark":"True"
    },

    "id96": {
        "example": "input: 123 \noutput: 321",
        "summary_prompt": ["Reverse digits in a number with a stack."],
        "prompts": ["Initialize a variable \"stack\" with an empty list, and \"num\" with {x} as a string.", "For each chracter in \"num\", append the character to \"stack\".", "Assign an empty string to a variable \"result\", and concatenate characters popped from the last element of \"stack\" to \"result\" until \"stack\" is empty.", "Cast \"result\" as integer and return it."],
        "test": "def check(candidate):\n    assert candidate(123) == 321\n    assert candidate(123456789) == 987654321\n    assert candidate(100) == 1\n    assert candidate(0) == 0\n    assert candidate(1230) == 321",
        "mark":"True"
    },

    "id97": {
        "example": "input: ['<<', '>>>'] \noutput: '>'",
        "summary_prompt": ["Calculate arrowheads left and right."],
        "prompts": ["Assign {x} to a variable \"arrows\", then concatenate all the strings in \"arrows\" and store the result to \"joined_arrow\".", "Count the numbers of left-facing arrow and right-facing arrow and store the results to \"left\" and \"right\", respectively.", "If \"right\" is larger than \"left\", return the string that consists of (right - left) right-facing arrows.", "Otherwise, return the string that consists of (left - right) left-facing arrows."],
        "test": "def check(candidate):\n    assert candidate(['<<', '>>>']) == '>'\n    assert candidate(['<<<', '>>']) == '<'\n    assert candidate(['<<', '>>', '<<', '>>>', '>>>']) == '>>>>'\n    assert candidate(['<<', '>>']) == ''\n    assert candidate(['<<<<<<<<<<<<', '>']) == '<<<<<<<<<<<'",
        "mark":"True"
    },

    "id98": {
        "example": "input: [1, 2, 3, 4, 5, 6, 8] \noutput: false",
        "summary_prompt": ["Check if the interval (max-min) is included in a list."],
        "prompts": ["Initialize an array \"array\" with {x}.", "Calculate the difference of maximum and minimum values in \"array\" and store the value to \"diff\".", "Check if \"diff\" is included in \"array\" and store the boolean value to \"result\".", "Return \"result\""],
        "test": "def check(candidate):\n    assert candidate([1, 2, 3, 4, 5, 6, 8]) == false\n    assert candidate([1, 7, 8]) == true\n    assert candidate([10]) == false\n    assert candidate([0, 1]) == true\n    assert candidate([1000, 2, 3, 4, 5, 6, 1000000]) == false",
        "mark":"True"
    },

    "id99": {
        "example": "input: 'aabbddcc' \noutput: 'a2b2d2c2'",
        "summary_prompt": ["Encode a string by converting repeated chars with counts."],
        "prompts": ["Initialize a variable \"original\" with \"{x}\"", "Import OrderedDict from collections module, then initalize a variable \"dic\" with an OrderedDict with letters in \"original\" as keys and 0 as the value for each key.", "Iterating over each character in \"original\", increment the value in \"dic\" whose key is the character.", "Initialize an empty string to a variable \"result\", then iterate over items in \"dic\" and append the key and the value as strings to \"result\".", "Return \"result\"."],
        "test": "def check(candidate):\n    assert candidate('aabbddcc') == 'a2b2d2c2'\n    assert candidate('abc') == 'a1b1c1'\n    assert candidate('zzzzzyyyyyxxxxxa') == 'z5y5x5a1'\n    assert candidate('aaa') == 'a3'\n    assert candidate('') == ''",
        "mark":"True"
    },

    "id100": {
        "example": "input: 'abc@example.com.' \noutput: 'abc'",
        "summary_prompt": ["Use regex to match email addresses and remove special chars."],
        "prompts": ["Import re and define a regular expression that matches an email address.", "Search for an email address in \"{x}\" and store the first match to a variable \"address\".", "Remove the substring starting from the @ symbol from \"address\".", "Replace non-alphabetical symbols with a whitespace in \"address\".", "Return \"address\"."],
        "test": "def check(candidate):\n    assert candidate('abc@example.com.') == 'abc'\n    assert candidate('a.b.c@example.com test.') == 'a b c'\n    assert candidate('a1b2c3.d4e_f6@example.com.') == 'a b c  d e f '\n    assert candidate('abc@example.com test. def@abc.def.') == 'abc'\n    assert candidate('example@@example.com test, example_email@abc.io .') == 'example email'",
        "mark":"True"
    },

    "id101": {
        "example": "input: [1, 3, 2, 2] \noutput: 2",
        "summary_prompt": ["Print out the second largest element in an array."],
        "prompts": ["Assign the list of numbers \"{A}\" to a variable named \"my_numbers\".", "Implement a function that returns the distinct elements of a list.", "Compute the distinct elements of my_numbers and store as unique_list.", "Return the second largest element in unique_list. If the second largest does not exit, return the maximum."],
        "test": "def check(candidate):\n    assert candidate([1, 3, 2, 2]) == 2\n    assert candidate([1000, 1000, 1000]) == 1000\n    assert candidate([0, 0.2, 0.4, -0.2]) == 0.2\n    assert candidate([3, 3, 3, 2, 2, 1]) == 2\n    assert candidate([0, 3, 1, 3, 2, 2, -0.2, 0.2]) == 2",
        "mark":"True"
    },

    "id102": {
        "example": "input: [1, 3, 2, 2] \noutput: 8",
        "summary_prompt": ["Return the largest prefix sum in an array."],
        "prompts": ["Assign the list of numbers \"{A}\" to a variable named \"my_numbers\".", "Implement a function that returns the prefix sum of a list as an array.", "Compute the prefix sum of my_numbers and store as prefix_sum_list.", "Return the largest element in prefix_sum_list. "],
        "test": "def check(candidate):\n    assert candidate([1, 3, 2, 2]) == 8\n    assert candidate([3, -3, -3]) == 3\n    assert candidate([0, 0.2, 0.4, -0.2]) == 0.6\n    assert candidate([3, 3, 3, -2, 2, 1]) ==10\n    assert candidate([-0.2,5,-0.2]) ==4.8",
        "mark":"True"
    },

    "id103": {
        "example": "input: [1,3,-4] \noutput: -4",
        "summary_prompt": ["Find the element which is the closest to zero and return it."],
        "prompts": ["Assign the list of numbers \"{A}\" to a variable named \"my_numbers\".", "Count the distances from each element in my_number to zero.", "Find the closest number to zero in my_number and store as closest_number.", "Return closest_number."],
        "test": "def check(candidate):\n   assert candidate([1,-4,-5])==-4\n   assert candidate([-5,-6,-7])== -5\n   assert candidate([-5,-6,-7])== -5\n   assert candidate([-5,-6,-7])== -5\n   assert candidate([-5,-6,-7])== -5",
        "mark":"True"
    },

    "id104": {
        "example": "input: 'acc' \noutput: 2",
        "summary_prompt": ["Find the max length contiguous subarray with unique characters."],
        "prompts": ["Assign the string \"{A}\" to a variable named \"my_string\".", "Implement a function that checks whether a string only contains unique characters.", "Find the longest substring of my_string that contains only unique characters and store as result_substring.", "Return the length of result_substring."],
        "test": "def check(candidate):\n    assert candidate('acc') == 2\n    assert candidate('accccccccccccccccccccc') == 2\n    assert candidate('abcdef') == 6\n    assert candidate('acdeffce') == 5\n    assert candidate('aaaaaaaaaaaaa') == 1",
        "mark":"True"
    },
    
     "id105": {
        "example": "input:'abadb' \noutput: 2",
        "summary_prompt": ["Print out the characters that appear most frequently."],
        "prompts": ["Assign a string \"{A}\" to a variable named \"my_string\", find the repeated characters in the my_string, count the frequency of these repeated characters, print out the length of most frequent character."],
        "test": "def check(candidate):\n    assert candidate('aaaaaaaa') == 8\n    assert candidate('caaaaaaaaaaaa') == 12\n    assert candidate('cccccaaaaa') == 5\n    assert candidate('abcde') == 0",
        "mark":"True"
    },

    "id106": {
        "example": "input:'a' \noutput: 1",
        "summary_prompt": ["Find the length of the longest callback substring."],
        "prompts": ["Assign a string \"{A}\" to a variable named \"my_string\", implement a function that checks whether a string is a palindrome, find all substrings of my_string which is a palindrome and store as a list, print out the length of longest palindrome in the above list."],
        "test": "def check(candidate):\n    assert candidate('abcba') == 5\n    assert candidate('caaa') == 3\n    assert candidate('cccccaaaaa') == 5\n    assert candidate('abcde') == 1",
        "mark":"True"
    },

    "id107": {
        "example": "input:10 \noutput: 4",
        "summary_prompt": ["Calculate the number of primes within a certain range."],
        "prompts": ["Assign an integer \"{A}\" to a variable named \"my_integer\", implement a function that checks whether an integer is a prime number, find all prime numbers that are less than my_integer and store as prime_result, print out the length of prime_result."],
        "test": "def check(candidate):\n    assert candidate(0) == 0\n    assert candidate(1) == 0\n    assert candidate(100) == 25\n    assert candidate(17) == 6",
        "mark":"True"
    },
    "id108": {
        "example": "input:[1, 2, 3, 4, 5], 3 \noutput: [3, 4, 5, 1, 2]",
        "summary_prompt": ["Rotate the array k steps to the right."],
        "prompts": ["Assign an array \"{A}\" to a variable named \"my_array\", assign a positive integer \"{K}\" to a variable named \"k\", implement a function that rotates one array to the right by 1 step, rotate my_array k steps and store as rotated_result, print out rotated_result."],
        "test": "def check(candidate):\n    assert candidate([-1, 30, 50, 3], 2) == [50, 3, -1, 30]\n    assert candidate([2, 3, 5, -30], 1) == [-30, 2, 3, 5]\n    assert candidate([1, 2, 0, 4], 0) == [1, 2, 0, 4]\n    assert candidate([2 ,3 ,4],8) == [3 ,4 ,2]",
        "mark":"True"
    },

    "id109": {
        "example": "input:[1, 2, 3, 4, 5] \noutput: 'False'",
        "summary_prompt": ["Checks whether an array can be divided into two equal subsets."],
        "prompts": ["Assign an array \"{A}\" to a variable named \"my_array\", compute the sum of my_array and store as my_sum, implement a function that checks whether one subset of an array \"{A}\" is equal to my_sum/2., print out the function output when the above array is my_array."],
        "test": "def check(candidate):\n    assert candidate([1 ,5 ,11 ,5]) == 'True'\n    assert candidate([1 ,2 ,3 ,5]) == 'False'\n    assert candidate([1 ,2 ,0 ,4]) == 'False'\n    assert candidate([2 ,3 ,4 ,3]) == 'True'",
        "mark":"True"
    },

    "id110": {
        "example": "input:2 \noutput: 1",
        "summary_prompt": [" Calculate the integral part of the square root."],
        "prompts": ["Assign a non-negative integer \"{A}\" to a variable named \"my_number\", compute the square root of my_number and store as root_number, implement a function that only returns the integer part of a float number, print out the integer part of root_number."],
        "test": "def check(candidate):\n    assert candidate(5) == 2\n    assert candidate(101) == 10\n    assert candidate(8) == 2\n    assert candidate(226) == 15",
        "mark":"True"
    },

    "id111": {
        "example": "input:2 \noutput: [3]",
        "summary_prompt": ["Add 1 to an integer and returns its number"],
        "prompts": ["Assign a non-negative integer \"{A}\" to a variable named \"my_number\", plus my_number by 1 and store as plus_number, implement a function that only returns the digits of an integer as a list, print out the digits of plus_number."],
        "test": "def check(candidate):\n    assert candidate(5) == [6]\n    assert candidate(101) == [1,0,2]\n    assert candidate(2345) == [2,3,4,6]\n    assert candidate(229) == [2,3,0]",
        "mark":"True"
    },

    "id112": {
        "example": "input:2\noutput: 'True'",
        "summary_prompt": ["Check if a non-negative integer is the sum of two square numbers."],
        "prompts": ["Assign a non-negative integer \"{A}\" to a variable named \"my_number\", implement a function that computes the square sum of two integers, implement a function that checks one number is the sum of two square numbers, print out \"True\" if my_number is the sum of two square numbers. Otherwise, print \"False\"."],
        "test": "def check(candidate):\n    assert candidate(5) == 'True'\n    assert candidate(101) == 'True'\n    assert candidate(3) == 'False'\n    assert candidate(7) == 'False'",
        "mark":"True"
    },

    "id113": {
        "example": "input:[14, 8, 11, 10] \noutput: 'False'",
        "summary_prompt": ["Determine if the standard deviation of an array is less than 1."],
        "prompts": ["Assign an array \"{A}\" to a variable named \"my_array\", implement a function that computes standard deviation of an array, calculate the standard deviation of my_array and store as result, print out \"True\" if result is less than 1. Otherwise, print \"False\"."],
        "test": "def check(candidate):\n    assert candidate([3 ,3 ,3 ,4]) == 'True'\n    assert candidate([1 ,1 ,1 ,1 ,1 ,101]) == 'False'\n    assert candidate([1 ,2 ,3 ,4 ,5 ,6 ,7]) == 'False'\n    assert candidate([1 ,0 ,1 ,0]) == 'True'",
        "mark":"True"
    },

    "id114":{
        "example": "input:[[3 ,2] ,[2 ,3]] \noutput: 4",
        "summary_prompt": ["Calculate the sum of the row and column numbers of a matrix."],
        "prompts": ["Assign the matrix \"{A}\" to a variable named \"my_matrix\", calculate the number of rows of my_matrix and store as row_number, calculate the number of columns of my_matrix and store as column_number, calculate the sum of row_number and column_number and print the result."],
        "test": "def check(candidate):\n    assert candidate([[3 ,2 ,5] ,[2 ,3 ,5]]) == 5\n    assert candidate([[1]]) == 2\n    assert candidate([[30000 ,30000 ,1] ,[30000 ,30000 ,1] ,[30000 ,30000 ,1]]) == 6\n    assert candidate([[5 ,5 ,5 ,5 ,5 ,0]]) == 7",
        "mark":"True"
    },

    "id115":{
        "example": "input:[3, 2, 2, 3] \noutput: 0",
        "summary_prompt": ["Calculate the difference between the mean and median of an array."],
        "prompts": ["Assign an array \"{A}\" to a variable named \"my_array\", calculate the mean of my_array and store as mean_number, calculate the median of my_array and store as median_number, calculate the difference between mean_number and median_number and print the result."],
        "test": "def check(candidate):\n    assert round(candidate([3, 2, 5, 2, 3, 5]),6) == round(0.3333333333333335 ,6)\n    assert candidate([1]) == 0\n    assert round(candidate([30000 ,30000 ,1 ,30000 ,30000 ,1 ,30000 ,30000 ,1]),6) == round(-9999.666666666668 ,6)\n    assert round(candidate([5 ,5 ,5 ,5 ,5 ,0]),6) == round(-0.833333333333333 ,6)",
        "mark":"True"
    }


 }
    
   

import os
import openai
from dotenv import load_dotenv, find_dotenv
import ast
import json
import codecs,yaml
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OPENAI_API_KEY')

def get_completion_from_messages(messages,
                                 model="gpt-3.5-turbo",
                                 temperature=0,
                                 max_tokens=500):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message["content"]


def clear_code(code):
    try:
        code = json.loads(code)
        code = code["code"]
    except:
        delimiter = "####"
        system_message = f"""
        You are now a smart programmer who needs to understand the instructions and outputs the correct code in Python mode according to user requirements\
        The customer service query will be delimited with \
        {delimiter} characters.\
        """

        user_message = f"""
        Here is an  example :\
        Q:"code": "def sum(m,n)\n    k = m+n    return k",\
         "explannation":"The code defines a function called 'sum' that takes m,n as input.  Finally, it returns the sum of m+n"\
        A:"def sum(m,n)\n    k = m+n    return k"\

        you need to copy the content of code from dictionary {code}\
        you mustn't copy the code about:"def sum(m,n)\n    k = m+n    return k"\
        make sure that the output is clear only with code without any expalnations\
           
        """
        messages = [
        {'role': 'system',
         'content': system_message},
        {'role': 'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]
        code = get_completion_from_messages(messages)
    return code

def general_code_generation(summary_prompt,example=None):
    delimiter = "####"
    system_message = f"""
    You are now a smart programmer who needs to output the correct code in Python mode according to user requirements\
    The customer service query will be delimited with \
    {delimiter} characters.\
    """

    user_message = f"""
    I want you to write a python code about define a function or class \\
    The task is {summary_prompt}\
    To help you have a better understanding we have the following instance to understand how it works:{example}\
    You must output the code in JSON format \
    and generate with the key: code,explanation\
    make sure that you mustn't generate code "\n" for so many times
    please use less than 20 words about explanation\
    please confirm that the code has a return\
    in order to distinguish it from your interpretation of the code\
    You must use brace to combine the code and explannation
    """
    
    messages = [
        {'role': 'system',
         'content': system_message},
        {'role': 'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]
    code = get_completion_from_messages(messages)
    code=clear_code(code)
    return code
    
def get_function_name(code):
    names = []

    tree = ast.parse(code)

    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            names.append(node.name)
        elif isinstance(node, ast.ClassDef):
            names.append(node.name)

    return names[0]


def get_decomposition(summary_prompt):
    mutiple_step=[]
    delimiter = "####"
    system_message = f"""
    You are a smart languager who only need decompose the  the contents according to user requirements\
    The customer service query will be delimited with \
    {delimiter} characters.\
    """

    user_message = f"""
    Let's think step by step\
    For example \
    the question:"Given the lengths of the four sides of the quadrilateral in an array, judge whether the quadrilateral is Cyclic"\
    the answer will be :
    "\
    1. The function is called "is_cyclic_quadrilateral",
    2. It takes one parameter, "sides", which is an array containing the lengths of the four sides of a quadrilateral.
    3. The purpose of the function is to determine whether the quadrilateral is cyclic or not.
    4. A cyclic quadrilateral is a quadrilateral that can be inscribed in a circle, meaning that all four vertices of the quadrilateral lie on the circumference of a circle.
    5. To determine if a quadrilateral is cyclic, we need to check if the sum of opposite angles is equal to 180 degrees.
    6. If the sum of opposite angles is equal to 180 degrees, then the quadrilateral is cyclic.
    7. If the sum of opposite angles is not equal to 180 degrees, then the quadrilateral is not cyclic.
    8. The function should return a boolean value, True if the quadrilateral is cyclic, and False if it is not."
    
    Now the question is :{summary_prompt}\
    please give me the answer in the similar way\
    """

    messages = [
        {'role': 'system',
         'content': system_message},
        {'role': 'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]
    mutiple_response = get_completion_from_messages(messages)
    mutiple_step = mutiple_response.split('\n')
    return mutiple_step


def step_code_generation(summary_prompt,step,example=None):
    delimiter = "####"
    system_message = f"""
    You are now a smart programmer who needs to output the correct code in Python mode according to user requirements\
    The customer service query will be delimited with \
    {delimiter} characters.\
    """

    user_message = f"""
    I want you to write only  a function or a class with some functions in python code  \
    please follow this rule all the time\
    you first need to write like'def 'or 'class'\
    the task is {summary_prompt}\
    To help you have a better understanding we have the following instance to understand how it works:{example}\
    To help you generate the code, i will give you each step\
    the steps are :{step}\
    
    
    You must output the code in JSON format \
    and generate with the key: code,explanation\
    make sure that must not react code "\n" for so many times\
    please use less than 100 words about explanation\
    please confirm that the code has a function name and a return as the final stop\
    in order to distinguish it from your interpretation of the code\
    You must use brace to combine the code and explannation
    """
    
    messages = [
        {'role': 'system',
         'content': system_message},
        {'role': 'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]
    code = get_completion_from_messages(messages)
    code = clear_code(code)
    return code

def step_cot_code_generation(summary_prompt,step,example=None):
    delimiter = "####"
    system_message = f"""
    You are now a smart programmer who needs to understand the instructions and outputs the correct code in Python mode according to user requirements\
    The customer service query will be delimited with \
    {delimiter} characters.\
    """

    user_message = f"""
    Let's think step by step\
    As the examples belowed\

    Example 1
    Q: Enter an integer array (list), and the function outputs the closest integer to the average of the array (rounded down if equidistant)\
    For example,inputs [1,2,3,4.1] outputss 3\
    To help generate the code, the steps are given\
    1. The function is called "find_closest_integer".\
    2. It takes one parameter, "array", which is an integer array (list)\.
    3. The purpose of the function is to find the closest integer to the average of the array.\
    4. To find the average of the array, we sum up all the elements and divide it by the length of the array.\
    5. We then find the closest integer to the average by comparing the absolute difference between each element and the average.\
    6. If there are multiple integers equidistant from the average, we round down to the lower integer.\
    7. The function should return the closest integer to the average.\
    8. If the array is empty, the function should return None.\
    
    A: 'Firstly,we can know that the value is a list with variables. \
    As we need to find the averages, we need to know the function average=sum substracts the number of variables\
    we can use len(inputs) to get the number of variables.\
    to get the sum ,we can use (for i in inputs)to get variables and save it with s,like s=s+i\
    After we get the average we can use \\ to get the range\
    compare the distance between average\\1 and average\\1+1\
    Finally , we can get the answer\
    'def closest_integer(value):\
       s=0\
       for i in value:\
          s=s+i\
       average=s/len(value)\
       if (average\\1-average)^2 > (average\\1+1-average)^2:\
           interger=average\\1+1\
       else:\
           interger=average\\1\
       return interger '
    
    I want you to write only  a function or a class with some functions in python code  \
    please follow this rule all the time\
    the task is {summary_prompt}\
    To help you have a better understanding we have the following instance to understand how it works:{example}\
    To help you generate the code, i will give you each step\
    the steps are :{step}\
    
    You must output the code in JSON format \
    and generate with the key: code,explanation\
    make sure that must not react code "\n" for so many times\
    please use less than 100 words about explanation\
    please confirm that the code has a function name and a return as the final stop\
    please make sure that the code has correct pattern like whther have correctly use "\n"\
    in order to distinguish it from your interpretation of the code\
    You must use brace to combine the code and explannation
   
    """
    
    messages = [
        {'role': 'system',
         'content': system_message},
        {'role': 'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]
    code = get_completion_from_messages(messages)
#     print(code)
    code = clear_code(code)
    return code


def eval_reward(code,code_t):
    
    name = get_function_name(code)
    code_composed= code + "\n" + code_t + "\n" + f"check({name})"   
    try:
        exec(code_composed )
        reward = 1  
    except:
        reward = 0 
    return reward


def test_code(datasets,id_number,example_use):
    
    reward_list=[]
    
    # mark
    code_mark = datasets[id_number]["mark"]
    print(f"""mark:{code_mark}""")
    print("\n")

    #test code
    code_t = datasets[id_number]["test"]
    print("test code")
    print(code_t)
    
    # whether use example
    if example_use==True:
        example=datasets[id_number]["example"]
    else:
        example=None
    
    # defination
    summary_prompt=datasets[id_number]["summary_prompt"]
    mtbp_prompt=datasets[id_number]["prompts"]
    id_decomposition=get_decomposition(summary_prompt)
    
    # five comparison
    # 0 baseline
    code_base= general_code_generation(summary_prompt,example=example)
    print("0 baseline")
    print(code_base)
    print("\n")
    reward_list.append(eval_reward(code_base,code_t))
    
    # 1 summary_prompt+decomposition
    code_de=step_code_generation(summary_prompt,id_decomposition,example=example)
    
    print("1 summary_prompt+decomposition")
    print(code_de)
    print("\n")
    reward_list.append(eval_reward(code_de,code_t))
    
    # 2 summary_prompt+mtbp_orignal
    code_mtbp=step_code_generation(summary_prompt, mtbp_prompt,example=example)
    print("2 summary_prompt+mtbp_orignal")
    print(code_mtbp)
    print("\n")
    reward_list.append(eval_reward(code_mtbp,code_t))
    
    # 3 summary_prompt+decomposition+chainofthought
    code_de_cot=step_cot_code_generation(summary_prompt, id_decomposition,example=example)
    print("3 summary_promptdecomposition+chainofthought")
    print(code_de_cot)
    print("\n")
    reward_list.append(eval_reward(code_de_cot,code_t))
    
    # 4 summary_prompt+mtbp_orignal+chainofthought
    code_mtbp_cot=step_cot_code_generation(summary_prompt, mtbp_prompt,example=example)
    print("4 summary_prompt+mtbp_orignal+chainofthought")
    print(code_mtbp_cot)
    print("\n")
    reward_list.append(eval_reward(code_mtbp_cot,code_t))
    

    return reward_list

#请输入字符串
id_number="id12"

print("id_number=",id_number)
print("\n")
reward_list=test_code(datasets,id_number,True)
print("reward_list=",reward_list)
print("################################################################################")
print("\n")