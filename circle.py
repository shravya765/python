class FileOwners:

    @staticmethod
    def group_by_owners(files):
        return files


files = {
    'Randy':'Input.txt' ,
    'Stan':'Code.py',
    'Randy':'Output.txt'
}

print(FileOwners.group_by_owners(files))