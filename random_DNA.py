import socket
import random
from Bio.Seq import translate


HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print request

    #Script goes here.
    dna_list = ["A","T","C","G"]
    organism_dna_list = []

    mut = random.choice(dna_list)
    length = len(mut)
    while length < 200:
        mut = mut + random.choice(dna_list)
        length = len(mut)

    prot = translate(mut)

    #Now its time to compose the html

    header = '''
    <html>
    <body>
    <h1>Random DNA </h1>
    '''

    random_DNA = "<br>>random_fasta_DNA<br>" + mut + "<br>"

    random_protein = "<br>>random_fasta_protein<br>" + prot + "<br>"

    footer = '''
    </body>
    </html>
    '''

    output = header + random_DNA + random_protein + footer


    http_response = str(output) #This holds the output.
    print output


    client_connection.sendall(http_response)
    client_connection.close()
