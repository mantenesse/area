#!/usr/bin/env python
if __name__ == '__main__':
        print 'Choose the shape for which you want to determine area:'
        print '(1) Square'

        shape_selection = raw_input()

        if shape_selection == '1':
                print 'Please enter the length of one side:'
                length = raw_input()
                area = int(length) * int(length)
                print 'The area is %i' % (area)
        else:
                print 'NOT A VALID SELCTION'
