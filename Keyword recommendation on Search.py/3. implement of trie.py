
class TrieNode:
    def __init__(self):
        self.child=[None]*26
        self.isEnd=False

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,key):
        curr=self.root
        for i in range(len(key)):
            index=ord(key[i])-ord("a")
            if curr.child[index]==None:
                curr.child[index]=TrieNode()
            curr=curr.child[index]
        curr.isEnd=True
    
    def search(self,key):
        curr=self.root
        for i in range(len(key)):
            index=ord(key[i])-ord("a")
            # print(chr(index+ord("a")))
            if curr.child[index]==None:
                return False
            curr=curr.child[index]
        return curr.isEnd

    def deleteM(self,root,key,i):
        if root is None:
            return None
        
        if i==len(key):
            root.isEnd=False
            if self.isEmpty(root):
                root=None
            return root

        indx=ord(key[i])-ord("a")
        root.child[indx]=self.deleteM(root.child[indx],key,i+1)
        if self.isEmpty(root) and root.isEnd==False:
            root=None
        return root

    def isEmpty(self,root):
        for b in range(26):
            if root.child[b] is not None:
                return False
        return True

    def delete(self,key):
        self.deleteM(self.root,key,i=0)


trie=Trie()

trie.insert("bad")
trie.insert("bat")
trie.insert("geek")
trie.insert("geeks")
trie.insert("cat")
trie.insert("cut")
trie.insert("zoo")


print(trie.search("cut"))
trie.delete("geeks")
print(trie.search("geeks"))

