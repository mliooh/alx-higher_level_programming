#include <stdio.h>

void print_python_list_info(PyObject *p)
{
    int size, alloc, index;
    PyVarObject *obj;

    size = Py_SIZE(p);
    alloc = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", alloc);

    for (index = 0; index < size; index++)
    {
        obj = PyList_GetItem(p, index);
        if (PyVarObject_Check(obj))
        {
            printf("Element %s: %s\n", index, Py_TYPE(obj)->tp_name);
        }
        else
        {
            printf("Error: Could not get element %d\n", index);
        }
    }
}
