import dropbox
 
class cloudstore:
    def __init__(self,key):
        self.key=key
    
    def upload(self,initial,final):
        drop = dropbox.Dropbox(self.key)

        locate=open(initial,'rb')
        drop.files_upload(locate.read,final)

def main():
    key = "Ra5Z9tL1xZwAAAAAAAAAAS_CbgFo1tE7h4iru8eknnp2HqpgdvdY_jsa_egb-b-A"
    filetobetransfered = cloudstore(key)
    initial=input("type out the present path of the file to be transfered ")
    final=input("ty")
    filetobetransfered.upload(initial,final)
    print("done")


main()
