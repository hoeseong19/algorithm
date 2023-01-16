class DisjointSet:
    def __init__(self):
        self.root = {}

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        # lexicographically smallest characters are heads
        if rootX <= rootY:
            self.root[rootY] = rootX
        else:
            self.root[rootX] = rootY


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        answer = ''

        disjoint_set = DisjointSet()

        for x, y in zip(s1, s2):
            if x not in disjoint_set.root:
                disjoint_set.root[x] = x
            if y not in disjoint_set.root:
                disjoint_set.root[y] = y
            disjoint_set.union(x, y)

        list_base_str = list(baseStr)
        for i, c in enumerate(list_base_str):
            if c in disjoint_set.root:
                list_base_str[i] = disjoint_set.find(c)

        answer = ''.join(list_base_str)

        return answer


print(Solution().smallestEquivalentString(
    s1="parker", s2="morris", baseStr="parser") == "makkek")
print(Solution().smallestEquivalentString(
    s1="hello", s2="world", baseStr="hold") == "hdld")
print(Solution().smallestEquivalentString(s1="leetcode",
      s2="programs", baseStr="sourcecode") == "aauaaaaada")
print(Solution().smallestEquivalentString(s1="cjgbnhojkkmgbmgddajmicdafgklkkdogaebeomcikdbafleihmjmbnmanokfbdkibhabdmdgbencabfikhnccjeceiolggbahnhcjgbnhojkkmgbmgddajmicdafgklkkdogaebeomcikdbafleihmjmbnmanokfbdkibhabdmdgbencabfikhnccjeceiolggbahnhcjgbnhojkkmgbmgddajmicdafgklkkdogaebeomcikdbafleihmjmbnmanokfbdkibhabdmdgbencabfikhnccjeceiolggbahnhcjgbnhojkkmgbmgddajmicdafgklkkdogaebeomcikdbafleihmjmbnmanokfbdkibhabdmdgbencabfikhnccjeceiolggbahnhcjgbnhojkkmgbmgddajmicdafgklkkdogaebeomcikdbafleihmjmbnmanokfbdkibhabdmdgbencabfikhnccjeceiolggbahnhcjgbnhojkkmgbmgddajmicdafgklkkdogaebeomcikdbafleihmjmbnmanokfbdkibhabdmdgbencabfikhnccjeceiolggbahnhcjgbnhojkkmgbmgddajmicdafgklkkdogaebeomcikdbafleihmjmbnmanokfbdkibhabdmdgbencabfikhnccjeceiolggbahnhcjgbnhojkkmgbmgddajmicdafgklkkdogaebeomcikdbafleihmjmbnmanokfbdkibhabdmdgbencabfikhnccjeceiolggbahnhcjgbnhojkkmgbmgddajmicdafgklkkdogaebeomcikdbafleihmjmbnmanokfbdkibhabdmdgbencabfikhnccjeceiolggbahnhcjgbnhojkkmgbmgddajmicdafgklkkdogaebeomcikdbafleihmjmbnmanokfbdkibhabdmdgbencabfikhnccjeceiolggbahnh",
      s2="gkcjamihkljkhonhcbableadmjfhofaomcfhgbifmendjhcgbgcejbnddijhbjjfmogjkamngcaodjknebfdnmdblikckcbicdejgkcjamihkljkhonhcbableadmjfhofaomcfhgbifmendjhcgbgcejbnddijhbjjfmogjkamngcaodjknebfdnmdblikckcbicdejgkcjamihkljkhonhcbableadmjfhofaomcfhgbifmendjhcgbgcejbnddijhbjjfmogjkamngcaodjknebfdnmdblikckcbicdejgkcjamihkljkhonhcbableadmjfhofaomcfhgbifmendjhcgbgcejbnddijhbjjfmogjkamngcaodjknebfdnmdblikckcbicdejgkcjamihkljkhonhcbableadmjfhofaomcfhgbifmendjhcgbgcejbnddijhbjjfmogjkamngcaodjknebfdnmdblikckcbicdejgkcjamihkljkhonhcbableadmjfhofaomcfhgbifmendjhcgbgcejbnddijhbjjfmogjkamngcaodjknebfdnmdblikckcbicdejgkcjamihkljkhonhcbableadmjfhofaomcfhgbifmendjhcgbgcejbnddijhbjjfmogjkamngcaodjknebfdnmdblikckcbicdejgkcjamihkljkhonhcbableadmjfhofaomcfhgbifmendjhcgbgcejbnddijhbjjfmogjkamngcaodjknebfdnmdblikckcbicdejgkcjamihkljkhonhcbableadmjfhofaomcfhgbifmendjhcgbgcejbnddijhbjjfmogjkamngcaodjknebfdnmdblikckcbicdejgkcjamihkljkhonhcbableadmjfhofaomcfhgbifmendjhcgbgcejbnddijhbjjfmogjkamngcaodjknebfdnmdblikckcbicdej", baseStr="rcomcrewoankfivfgfcfkgeadtnmhagjczisqblyldidsuhfdsooviilaaosgswjbqzhkwfwdgqbnuypegvsqoborpnhtjjaxcpjwtxowutansksxzzydoottmknysmpxyetwhlghwbwqvsasmwjsdcgzgfudhettrasxayqdtjkykeyxvqzuvwtlfnoyvauiilqtfstoeilmzbncnxildnjaaoxezuflkthcgdjneycktavzmsovdtxpxjtcfxfkyvsfxnzrwdnnjcnkplctexlgqzipfvqcxfawzdznhbhtdkhfoirliqdfehsiviiimntnuzyfhnbgxakhozldclhxjzpgzyabxwrrfalqdfeaxtvkkucslhrypsjexjdhbeuuckolfgrvxecuhslcbezuxsoklmqpmobybqausuneushwgrrtafujsljzpprklapncxlwktpitejlujycahvvfvggrzayolskjvaauocfikptwiyntvqejfdxirsbmqqrilnmcopskbtdlozevmbiaxraspymfnyaxgazfxsuoygeqzoccmsxamtpcquxvrpsqzdqxaaouyjnrmqxlsvfwsfnmeqyvvufkvlzhzpsfqojrdntpxekahrknbrjtzmhrasbynxwnzfoishiaqmomkcgfsokrdmxmjyxrmrsaphcxicbfubzbvaeuevvvsidhgtzhxevtjxwiwriqkomltbaenbgxxdvzdcuddixkudbcoplqvyyzrkkkjxlqilowootcapiygayfpqzlhdfemmweynumqocfjlicesvbziglxvuqrimxbntrpaebvcbvdeqkepgnejlfkynpqzfamfylvogkakhgeuqqiegsvjoxjfgoiadlevwnwdwyljvvdzrzgiryhmepannhyfzvzxxbaxnqfrgnpksxomdojqvquwqagomfjubsrkxmnwdwfixbwmegdljzcjtdonufsoweesjlvjqivx"))
