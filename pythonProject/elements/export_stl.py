# STL exporter
import os.path


def export_stl_2(file_name, label, x, y, z, ox, oy, oz):
    """
    generates an stl file containing one board with given dimensions (x,y,z) and offset (ox, oy, oz)
    can be used in a loop
    :param file_name: name of the STL file to export to
    :param label: label of the piece being written
    :param x: size on x axis
    :param y: size on y axis
    :param z: size on z axis
    :param ox: orientation on x axis
    :param oy: orientation on y axis
    :param oz: orientation on x axis
    :return: n/a
    """
    name = file_name + ".stl"

    with open(name, mode='a') as stl_file:
        stl_file.write('solid ' + label + '\n')

        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')

        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')

        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')

        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')

        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')

        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')

        #		stl_file.write('    vertex 0.0 0.0 0.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 0.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex 0.0 0.0 '+str(z)+'.0'+'\n')

        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        #		stl_file.write('    vertex 0.0 '+str(y)+'.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex 0.0 0.0 0.0'+'\n')
        #		stl_file.write('    vertex 0.0 0.0 '+str(z)+'.0'+'\n')

        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        #		stl_file.write('    vertex 0.0 0.0 0.0'+'\n')
        #		stl_file.write('    vertex 0.0 '+str(y)+'.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex 0.0 '+str(y)+'.0 0.0'+'\n')

        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        #		stl_file.write('    vertex 0.0 '+str(y)+'.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 '+str(y)+'.0 0.0'+'\n')
        #		stl_file.write('    vertex 0.0 '+str(y)+'.0 0.0'+'\n')

        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        #		stl_file.write('    vertex '+str(x)+'.0 '+str(y)+'.0 0.0'+'\n')
        #		stl_file.write('    vertex 0.0 '+str(y)+'.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 '+str(y)+'.0 '+str(z)+'.0'+'\n')

        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        #		stl_file.write('    vertex '+str(x)+'.0 '+str(y)+'.0 0.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 0.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 0.0 0.0'+'\n')

        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        #		stl_file.write('    vertex '+str(x)+'.0 0.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 '+str(y)+'.0 0.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 '+str(y)+'.0 '+str(z)+'.0'+'\n')

        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('endsolid ' + label + '\n')


def export_stl(file_name, label, x, y, z, ox, oy, oz):
    """
    generates an stl file containing one board with given dimensions (x,y,z) and offset (ox, oy, oz)
    can be used in a loop
    :param file_name: name of the STL file to export to
    :param label: label of the piece being written
    :param x: size on x axis
    :param y: size on y axis
    :param z: size on z axis
    :param ox: orientation on x axis
    :param oy: orientation on y axis
    :param oz: orientation on x axis
    :return: n/a
    """
    file_name = file_name + ".stl"

    if not os.path.exists(file_name):
        print("Create file and add the 'solid' line")
        create_new_file(file_name)
        print("Write the board to write")
        write_board(file_name, label, x, y, z, ox, oy, oz)
        print("write the end solid")

    else:
        print("delete last row from file")
        delete_last_row(file_name)
        print("Write the board to write")
        write_board(file_name, label, x, y, z, ox, oy, oz)
        print("write the end solid")


def create_new_file(file_name):
    with open(file_name, mode='a') as stl_file:
        stl_file.write('solid ' + file_name + '\n')
    stl_file.close()


def delete_last_row(file_name):

    with open(file_name, mode='r') as stl_file:
        data = stl_file.readlines()
        data[len(data)-1] = ""
        print(data)
    stl_file.close()

    with open(file_name, mode='w') as stl_file:
        stl_file.writelines(data)
    stl_file.close()


def write_board(file_name, label, x, y, z, ox, oy, oz):
    with open(file_name, mode='a') as stl_file:

        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')

        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')

        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')

        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')

        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')

        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')

        #		stl_file.write('    vertex 0.0 0.0 0.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 0.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex 0.0 0.0 '+str(z)+'.0'+'\n')

        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        #		stl_file.write('    vertex 0.0 '+str(y)+'.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex 0.0 0.0 0.0'+'\n')
        #		stl_file.write('    vertex 0.0 0.0 '+str(z)+'.0'+'\n')

        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        #		stl_file.write('    vertex 0.0 0.0 0.0'+'\n')
        #		stl_file.write('    vertex 0.0 '+str(y)+'.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex 0.0 '+str(y)+'.0 0.0'+'\n')

        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        #		stl_file.write('    vertex 0.0 '+str(y)+'.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 '+str(y)+'.0 0.0'+'\n')
        #		stl_file.write('    vertex 0.0 '+str(y)+'.0 0.0'+'\n')

        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        #		stl_file.write('    vertex '+str(x)+'.0 '+str(y)+'.0 0.0'+'\n')
        #		stl_file.write('    vertex 0.0 '+str(y)+'.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 '+str(y)+'.0 '+str(z)+'.0'+'\n')

        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        #		stl_file.write('    vertex '+str(x)+'.0 '+str(y)+'.0 0.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 0.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 0.0 0.0'+'\n')

        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('facet normal 0.0 0.0 0.0' + '\n')
        stl_file.write('  outer loop' + '\n')
        #		stl_file.write('    vertex '+str(x)+'.0 0.0 '+str(z)+'.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 '+str(y)+'.0 0.0'+'\n')
        #		stl_file.write('    vertex '+str(x)+'.0 '+str(y)+'.0 '+str(z)+'.0'+'\n')

        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy) + '.0 ' + str(oz + z) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz) + '.0' + '\n')
        stl_file.write('    vertex ' + str(ox + x) + '.0 ' + str(oy + y) + '.0 ' + str(oz + z) + '.0' + '\n')

        stl_file.write('  endloop' + '\n')
        stl_file.write('endfacet' + '\n')
        stl_file.write('endsolid ' + file_name + '\n')
    stl_file.close()
