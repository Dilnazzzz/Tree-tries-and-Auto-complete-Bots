# Tree Tries and Auto-complete Bots

Auto-completion functionalities are now ubiquitous in search engines, document editors, and messaging apps. Here, I built an auto-complete engine. 

A trie tree, or a prefix tree, is a common data structure that stores a set of strings in a collection of nodes so that all strings with a common prefix are found in the same branch of the tree. Each node is associated with a letter, and as you traverse down the tree, you pick up more letters, eventually forming a word. Complete words are commonly found on the leaf nodes. However, some inner nodes can also mark full words.

Several important features of tries:

1. Nodes that mark valid words are marked in yellow. Notice that while all leaves are considered valid words, only some inner nodes contain valid words, while some remain only prefixes to valid words appearing down the branch.

2. The tree does not have to be balanced, and the height of different branches depends on its contents.

3. In our implementation, branches never merge to show common suffixes (for example, both ANT and ART end in T, but these nodes are kept separate in their respective branches). However, this is a common first line of memory optimization for tries.

4. The first node contains an empty string; it “holds the tree together.”

Here, I implemented a functional trie tree. I inserted words into a dictionary, looked up valid and invalid words, printed your dictionary in alphabetical order, and suggested appropriate suffixes like an auto-complete bot.
