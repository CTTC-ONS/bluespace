from swagger_server.models.operation import Operation

operations = list()


def create_operation(arof_id, enable):
    """
    Create operation by ID

    :param arof_id: arof id
    :type arof_id: int
    :param enable: enable or disable the laser
    :type enable: bool

    :return: new operation
    :rtype: Operation
    """
    if len(operations) != 0:  # if exists operations
        if not any(id for (id, op) in enumerate(operations) if
                   op.arof_id == arof_id):  # if not exists arof_id in operations
            return new_operation(arof_id, enable)
    else:
        return new_operation(arof_id, enable)


def new_operation(arof_id, enable):
    """
    Create and add operation to operations

    :param arof_id: arof id
    :type arof_id: int
    :param enable: enable or disable the laser
    :type enable: bool

    :return: new operation
    :rtype: Operation
    """
    new_op = Operation(arof_id, enable)
    operations.append(new_op)
    return new_op


def update_operation(arof_id, enable):
    """
    Update operation by ID

    :param arof_id: arof id
    :type arof_id: int
    :param enable: enable or disable the laser
    :type enable: bool

    :return: operation modified
    :rtype: Operation
    """
    index = next((index for (index, p) in enumerate(operations) if p.arof_id == arof_id), None)
    # returns the index position if arof id exist in list of operations. None, otherwise
    if index is not None:  # if arof id exists
        operations[index].arof_id = arof_id
        operations[index].enable = enable
        return operations[index]
    else:
        return new_operation(arof_id, enable)


def delete_operation(arof_id):
    """
    Delete operation by ID

    :param arof_id: arof id
    :type arof_id: int
    """
    if len(operations) != 0:  # if exists operations
        for op in operations:
            if op.arof_id == arof_id:
                operations.remove(op)
