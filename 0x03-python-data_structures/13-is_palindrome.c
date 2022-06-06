#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * intatindex - checks the integer value at index values
 * @index1: first index to check Number
 * @index2: second index to check Number
 * @head: address of the head of list
 *
 * Return: 1 if numbers are the same and 0 if different
 */

int intatindex(listint_t *head, unsigned int index1, unsigned int index2)
{
	listint_t *ptr = head;
	unsigned int n = 1;
	int A, J;

	while (ptr != NULL)
	{
		if (n == index1)
			A = ptr->n;
		if (n == index2)
		{
			J = ptr->n;
			break;
		}
		ptr = ptr->next;
		n++;
	}
	if (A == J)
		return (1);
	else
		return (0);
}
/**
 * lent - counts to the end of list
 * @head: address of head list
 *
 * Return: length of list
 */

int lent(listint_t *head)
{
	int n = 1;
	listint_t *ptr = head;

	while(ptr->next != NULL)
	{
		n++;
		ptr = ptr->next;
	}
	return (n);
}

/**
 * is_palindrome - checks if a list is palindrome
 * @head: address of head of the list
 *
 * Return: 0 if false and 1 if true
 */

int is_palindrome(listint_t **head)
{
	listint_t *ptr = *head;
	int check = 0;
	int len;
	int i;

	if (ptr == NULL || ptr->next == NULL)
		return (1);
	else
	{
		len = lent(ptr);
		for (i = 1; i <= (len/2); i++)
		{
			check = intatindex(ptr, i, len - i + 1);
			if (check == 0)
				break;
		}
		return (check);
	}
}
