#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 * nodeptr - creates memory
 * add: address of allocated memory
 * curr: current address being examine
 * num: number to compare with
 *
 * Return: no shit
 */

void nodeptr(listint_t *add, listint_t *curr, int num)
{
	listint_t *temp = NULL;

	while (curr != NULL)
	{
		if (num < curr->n)
		{
			add->next = curr;
			temp->next = add;
			break;
		}

		else
		{
			temp = curr;
			curr = curr->next;
		}
	}
	if (curr == NULL)
		temp->next = add;
}

/**
 * insert_node - insert node sortically
 * head: head of list
 * number: number to be added
 *
 * Return: address
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr = NULL;
	listint_t *h = *head;

	ptr = malloc(sizeof(listint_t));
	if (ptr == NULL)
		return (NULL);
	ptr->n = number;
	ptr->next = NULL;

	if (h == NULL)
	{
		ptr->next = NULL;
		*head = ptr;
	}
	else if (h->n > number)
	{
		ptr->next = *head;
		*head = ptr;
	}
	else
		nodeptr(ptr, h, number);
	return (ptr);
}
