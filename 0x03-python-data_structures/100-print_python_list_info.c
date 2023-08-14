#include <Python.h>

/**
 * print_python_list_info - this prints the basic info about
 * python lists
 * @p: a PyObject list
 */

void print_python_list_info(PyObject *p)
{
	int size, alloc, j;
	PyObject *item;

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (j = 0; j < size; j++)
	{
		item = PyList_GetItem(p, j);
		printf("Element %d: %s\n", j, Py_TYPE(item)->tp_name);
	}
}
