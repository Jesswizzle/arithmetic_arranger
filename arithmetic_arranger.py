def arithmetic_arranger(problems, show_answers=False):

  #Check if the number of problems is less than five
  #Indent!!
  if len(problems) > 5:
    return "Error: Too many problems."

  #Define arranged_problems so you don't have issues later
  arranged_problems = {"top": [], "bottom": [], "line": [], "answer": []}

  #Loop through the problems
  for problem in problems:

    #Split problem into subjects and actions
    #Indent!!
    subject1, actions, subject2 = problem.split()

    #Check if the actions are valid
    if actions not in ['+', "-"]:

      #INDENT
      return "Error: Operator must be '+' or '-'."

    #Check if subjects only digits
    if not subject1.isdigit() or not subject2.isdigit():

      #Indent (please)
      return "Error: Numbers must only contain digits."

    #Check if subjects 4 digits
    if len(subject1) > 4 or len(subject2) > 4:

      #IDK how far to indent here but anyway
      return "Error: Numbers cannot be more than four digits."

    #Maximum width of subjects
    max_width = max(len(subject1), len(subject2))

    #Formatted strings for arranged problems
    #I won't indent here because no :?
    arranged_problems["top"].append(subject1.rjust(max_width + 2))
    arranged_problems["bottom"].append(actions + subject2.rjust(max_width + 1))
    arranged_problems["line"].append('-' * (max_width + 2))

    #Calculate show_answers == True
    if show_answers:
      if actions == '+':
        answer = str(int(subject1) + int(subject2))
      else:
        answer = str(int(subject1) - int(subject2))
      arranged_problems["answer"].append(str(answer).rjust(max_width + 2))

  #Join formatted strings with spaces
  #This is going in the same indent as for loop
  top_line = '    '.join(arranged_problems["top"])
  bottom_line = '    '.join(arranged_problems["bottom"])
  line_line = '    '.join(arranged_problems["line"])

  arranged_output = f"{top_line}\n{bottom_line}\n{line_line}"

  #If show_answers True == True
  if show_answers:
    answer_line = '    '.join(arranged_problems["answer"])
    arranged_output += f'\n{answer_line}'

  return arranged_output
