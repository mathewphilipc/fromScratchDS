import random
grammar = {
"_S" : ["_NP _VP"],
"_NP" : ["_N",
"_A _NP _P _A _N"],
"_VP" : ["_V",
"_V _NP"],
"_N" : ["data science", "Python", "regression"],
"_A" : ["big", "linear", "logistic"],
"_P" : ["about", "near"],
"_V" : ["learns", "trains", "tests", "is"]
}

def is_terminal(token):
	return token[0] != "_"
	
def expand(grammar, tokens):
	for i, token in enumerate(tokens):

		# skip over terminals
		if is_terminal(token): continue

		# if we get here, we found a non-terminal tokaen
		# so we need to choice a replacement at random
		replacement = random.choice(grammar[token])

		if is_terminal(replacement):
			tokens[i] = replacement
		else:
			tokens = tokens[:i] + replacement.split() + tokens[(i+1):]

		# now call expand on the new list of tokens
		return expand(grammar, tokens)
	# if we get here, everything is terminal and we are done
	return tokens

def generate_sentence(grammar):
	return expand(grammar, ["_S"])

print(' '.join(generate_sentence(grammar)))