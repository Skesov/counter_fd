def count_fd():
    """ Return a string with number of open descriptors or error """
    try:
        with open('/proc/sys/fs/file-nr') as f:
            data = f.read()

        list_of_data = data.split()

        total_allocated_fd = int(list_of_data[0])
        total_free_allocated_fd = int(list_of_data[1])

        opened_fd = total_allocated_fd - total_free_allocated_fd

        return str(opened_fd)

    except Exception as error:

        return error
