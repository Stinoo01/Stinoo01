#creating function
def mass(protein):
    #creating dictionary with the corresponding mass
    dictionary = {
        'A': 71.03711,
        'C': 103.00919,
        'D': 115.02694,
        'E': 129.04259,
        'F': 147.06841,
        'G': 57.02146,
        'H': 137.05891,
        'I': 113.08406,
        'K': 128.09496,
        'L': 113.08406,
        'M': 131.04049,
        'N': 114.04293,
        'P': 97.05276,
        'Q': 128.05858,
        'R': 156.10111,
        'S': 87.03203,
        'T': 101.04768,
        'Y': 163.06333,
        'W': 186.07931,
        'V': 99.06841,
        }
    #summing all the masses of the protein
    #summing eache letter and its corresponding value    
    result = sum([dictionary[x] for x in protein])
    #returning the result 
    return result

#taking data and printing result 
a = 'QYFGHGPDFTIIGNCQWEWPWVTVGPHPVDAHGLMSALWAPRTSWTEPWQATMQLLHWHTAWSNDAFECDCALAMHGITPTIQCCWVMRKTRHHNHREFDQICCHYVEKDWLQIQLFGVRHIEYMDWQTFQESIANEGEWHKEIMSPLMEDSRGMLQWPFLRKYQRGIHAWQRHPWWQHECYLLICADAGKWARNYVTICPYMIELQGKTSISDSTRKCKNEYWWHNRVICANDRRLFTAWFYVHLWENHKQHCYILVYCYQPDKWKYLQVQTTLVPVFDQYHRYSCSPMGLMINHTHFLRDLNPEWWGKIHYMCPHCEVCCHLCKDCDYMWVGCTHPNMRGNNRVLYAVIQWVCLWIEFFEMFKDTMDRHIMNFIPHMQMNTQLVKITIHLWPILRDENRPMNQEMWFCEEIKQAMELALFSSYWTEHHDPAHFGFSAYHHVFAKCMYLFQGPHKYVPGGCMTAWDCDVVPNWCWQEQMFMMDPQTPPWMWLGMNHYKRYQHHMMNTDQPVLNNTTFIKAEKRVECATKCGCMSQYSRESGNFQHWAHSTFLYYNNRGHTKVQSYTEEKRTRDQFIWWWYAVHPFLRSMRPYMQMMGFWDSDLARTRERHNLELDVVGKNCDLHNDWIENKIRCPSVWVLPGDITGYCEMLMIVQQPDPIRHATACMQFQDFPWEHGDHNEQYVDLTVKFKSHKQDLAYNNEVNCNFGPECGILESPPETMWLQWDQLSIWYTAICSNSEGMSNGMCQCIKPIDYGHILAAWLNTLNQQCDWSYAPHNGIQSETNMLSQYNQQWCTNPDCNQ'
print(mass(a))
