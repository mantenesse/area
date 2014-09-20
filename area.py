#!/usr/bin/env python
if __name__ == '__main__':
        print 'Choose the shape for which you want to determine area:'
        print '(1) Square'
        print '(2) rectangle'
        print '(3) sircle'
        shape_selection = raw_input()

        if shape_selection == '1':
                print 'Please enter the length of one side:'
                length = raw_input()
                area = int(length) * int(length)
                print 'The area is %i' % (area)
        elif shape_selection =='2':
                print 'Please enter the length of one side:'
                length = raw_input()
                print 'Please enter the width of one side:'
                width = raw_input()
                area = int(length) * int(width)
                print 'The area is %i' % (area)
        elif shape_selection =='3':
                print 'Please enter the radeus:'
                radeus = raw_input()
                area = int(radeus)*3*int(radeus)
                print 'The area is %i' % (area)
                
        else:
                print 'NOT A VALID SELCTION'



