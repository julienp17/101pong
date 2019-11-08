##
## EPITECH PROJECT, 2019
## 101pong
## File description:
## Makefile
##

MAIN = src/main.py

NAME = 101pong

all: $(NAME)

$(NAME):
	cp $(MAIN) ./$(NAME)
	chmod +x $(NAME)

tests_run:
	@python -m unittest discover test/

fclean:
	rm -f $(NAME)

re: fclean all