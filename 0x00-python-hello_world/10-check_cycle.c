#include "lists.h"

/**
 * check_cycle - prints all elements of a listint_t list
 * @list: pointer to head of list
 * Return: number of nodes
 */

int check_cycle(listint_t *list)
{
	listint_t *node = list->next;

	if (list == NULL)
		return (0);

	while (node && node != list)
		node = node->next;

	return (node == list);
}
