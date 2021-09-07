#include "lists.h" 

/**
 * check_cycle - prints all elements of a listint_t list
 * @list: pointer to head of list
 * Return: number of nodes
 */

int check_cycle(listint_t *list)
{
	if (list == NULL)
		return (0);

	listint_t *node = list->next;

	while (node && node != list)
		node = node->next;

	return (node == list);
}
