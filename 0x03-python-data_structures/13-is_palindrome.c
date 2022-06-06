#include <stdlib.h>
#include <stdio.h>
#include "lists.h"


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

	while (ptr->next != NULL)
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
	int *list = NULL;
	int n = 0;
	int J = 1;
	int i;

	if (ptr == NULL || ptr->next == NULL)
		return (1);
	n = lent(ptr);
	list = malloc(sizeof(int) * n);
	if (list == NULL)
	{
		perror("try again");
		exit(0);
	}
	for (i = 0; i < n; i++)
	{
		list[i] = ptr->n;
		ptr=ptr->next;
	}
	for (i = 0; i < (n / 2); i++)
	{
		if (list[i] != list[n - i - 1])
		{
			J = 0;
			break;
		}
	}
	free(list);
	return (J);
}
