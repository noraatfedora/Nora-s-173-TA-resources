#
# File: Makefile
# Creator: George Ferguson, modified by Nora Goodman
# Created: Thu Jun 30 11:00:49 2016
#
# Sample Makefile for a "Hello World" c project
#
# This Makefile builds the test programs for the data structures
# distributed with the bundle, and show how you might use it to
# build YOUR program for the project.
#


CFLAGS = -g -std=c99 -Wall -Werror -pedantic

PROG = hello_world
SRCS = hello.c -lm
OBJS = ${SRCS:%.c=%.o}

$(PROG): $(OBJS)
	$(CC) -o $(PROG) $(OBJS)
