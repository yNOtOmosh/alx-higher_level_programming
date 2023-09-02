#include <stdio.h>
#include "Python.h"

/**
 * print_python_string - print a string
 * @p: is a pyobject string object.
*/
void print_python_string(PyObject *p)
{
  if (!PyUnicode_Check(p))
  {
    PyErr_SetString(PyExc_TypeError, "Invalid Python string obect");
    return:
  }

  const char *str = PyUnicode_AsUFT8(p);

  if (str == NULL)
  {
    PyErr_SetString(PyExc_RuntimeError, "failed to decode Python string");
    return;
  }

  printf("%s\n", str);
}
