"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Daniela Gutierrez, this 
programming assignment is my own work and I have not provided this code to 
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: adg4258
"""

def length_of_longest_substring_n3(s):
     max_length = 0

     for i in range(len(s)):
            for j in range(i, len(s)):
                  substr = s[i:j+1]
                  if len(set(substr)) == len(substr):
                        max_length = max(max_length, len(substr))

     return max_length

def length_of_longest_substring_n2(s):
      max_length = 0

      for i in range(len(s)):
            freq_list = [0] * 256

            for j in range(i, len(s)):
                  char_index = ord(s[j])
                  freq_list[char_index] += 1

                  if freq_list[char_index] > 1:
                        break
                  max_length = max(max_length, j - i + 1)

      return max_length


def length_of_longest_substring_n(s):
    max_length = 0
    left = 0
    char_index = {}

    for right in range(len(s)):
          char = s[right]

          if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1

          char_index[char] = right

          max_length = max(max_length, right - left + 1)

    return max_length
