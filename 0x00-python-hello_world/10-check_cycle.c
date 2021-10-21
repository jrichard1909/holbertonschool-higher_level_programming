#include "lists.h"

/**
 * check_cycle - prints all elements of a listint_t list
 * @list: pointer to head of list
 * Return: number of nodes
 */

int check_cycle(listint_t *list)
{
	listint_t *temp1, *temp2;

	temp1 = list;
	temp2 = list;

	while (list)
	{
		temp2 = temp2->next;
		if (!temp1 || !temp2)
			return (0);
		if (temp2 == temp1)
			return (1);
	}
	return (0);
}
