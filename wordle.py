import re

final_render = {
	"top": "",
	"middle": "",
	"bottom": ""
}

render_type = {
	"ABSENT": 1,
	"PRESENT": 2,
	"CORRECT": 3,
}
renders = {
	"ABSENT": ("--- ", "|{0}| ", "--- "),
	"PRESENT": ("?-? ", "|{0}| ", "?-? "),
	"CORRECT": ("+++ ", "+{0}+ ", "+++ ")
}

def find_occurrence(word, letter):
	return [x.start() for x in re.finditer(letter, word)]

def add_render(type, *letter):
	if type in render_type:
		render = renders[type]
		final_render["top"] += render[0]
		final_render["middle"] += render[1].format(letter[0])
		final_render["bottom"] += render[2]

def finalize_render():
	print(final_render["top"])
	print(final_render["middle"])
	print(final_render["bottom"])

	# clear render
	final_render["top"] = ""
	final_render["middle"] = ""
	final_render["bottom"] = ""
	
def check(word, attempt):
	position = -1
	correct = 0
	previous, count  = None, 0
	for letter in attempt:
		position += 1
		if not letter in word:
			add_render("ABSENT", letter)
		else:
			# checks for duplicate letters
			if previous != None:
				if previous == letter:
					count += 1
				else:
					count = 1

			# print(position)
			# print(find_occurrence(word, letter))
			# print(position in find_occurrence(word, letter))
			if position in find_occurrence(word, letter):
				# print("corr")
				add_render("CORRECT", letter)
				correct += 1
			else:
				# print(count, word.count(letter), letter)
				if count > word.count(letter):
					add_render("ABSENT", letter)
				else:
					add_render("PRESENT", letter)
				
			previous = letter
					
	finalize_render()
	
	return correct == len(word)
if __name__ == "__main__":
	add_render("ABSENT", "a")
	add_render("PRESENT", "b")
	add_render("CORRECT", "c")

	finalize_render()