# Wizard free vault

Catagory | Points | Players solved
---------|--------|---------------
Reverse Engineering | 200 | ???

## Description

???

## Solution

The challenge is sequential so let's go step by step.

### Step 1

[Here's first step.](https://github.com/siddhpant/Junior-InCTF-2017-Writeup/blob/4db4503fa4c9658eb39869983c35c852778eaf69/Reverse%20Engineering/(200)%20Wizard-free-vault/muggles.py#L13)

```python
inp1=raw_input("LEVEL 1: \n Enter the password:").strip('\n')
obj_1.update(inp1)
if cmp("8a0e2e33fc0ef5f4d1b9243139a2aa4f",str(obj_1.hexdigest())) == 0:
print "Well.. I still think that you are a squib"
```

Hmm... `obj1` is defined at the top as `hashlib.md5()`, so it's essentially `hashlib.md5().hexdigest`, that means it's comparing the MD5 hash of our input. This means we can reverse search for it, [and it turns out to be "Muggles"](https://hashtoolkit.com/reverse-hash/?hash=8a0e2e33fc0ef5f4d1b9243139a2aa4f).

Yay we passed our first check!

### Step 2

[Here's step 2, ends at line 26](https://github.com/siddhpant/Junior-InCTF-2017-Writeup/blob/4db4503fa4c9658eb39869983c35c852778eaf69/Reverse%20Engineering/(200)%20Wizard-free-vault/muggles.py#L17)

Muggle numbers! :thinking:

The code is taking the numbers, then puts it in a list after 

(I will complete this later).....
