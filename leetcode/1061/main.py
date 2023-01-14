from collections import defaultdict, deque
from heapq import heappop, heappush


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        answer = ''

        graph = defaultdict(set)

        dict_char_TO_lexicographically_smallest_equivalent_char = {}

        length_string = len(s1)

        for i in range(length_string):
            graph[s1[i]].add(s2[i])
            graph[s2[i]].add(s1[i])

        def bfs(char):
            list_equivalent_char = []
            q_char = deque([char])

            while q_char:
                c = q_char.popleft()

                heappush(list_equivalent_char, c)

                for equivalent_char in graph[c]:
                    if equivalent_char not in list_equivalent_char:
                        q_char.append(equivalent_char)

            lexicographically_smallest_equivalent_char = heappop(
                list_equivalent_char)

            for equivalent_char in list_equivalent_char:
                dict_char_TO_lexicographically_smallest_equivalent_char[
                    equivalent_char] = lexicographically_smallest_equivalent_char

        set_string = set(s1).union(set(s2))

        for c in set_string:
            if c not in dict_char_TO_lexicographically_smallest_equivalent_char:
                bfs(c)

        for k, v in dict_char_TO_lexicographically_smallest_equivalent_char.items():
            baseStr = baseStr.replace(k, v)

        answer = baseStr

        return answer


# print(Solution().smallestEquivalentString(
#     s1="parker", s2="morris", baseStr="parser") == "makkek")
# print(Solution().smallestEquivalentString(
#     s1="hello", s2="world", baseStr="hold") == "hdld")
# print(Solution().smallestEquivalentString(s1="leetcode",
#       s2="programs", baseStr="sourcecode") == "aauaaaaada")

print(Solution().smallestEquivalentString(s1 = "cjgbnhojkkmgbmgddajmicdafgklkkdogaebeomcikdbafleihmjmbnmanokfbdkibhabdmdgbencabfikhnccjeceiolggbahnhcjgbnhojkkmgbmgddajmicdafgklkkdogaebeomcikdbafleihmjmbnmanokfbdkibhabdmdgbencabfikhnccjeceiolggbahnhcjgbnhojkkmgbmgddajmicdafgklkkdogaebeomcikdbafleihmjmbnmanokfbdkibhabdmdgbencabfikhnccjeceiolggbahnhcjgbnhojkkmgbmgddajmicdafgklkkdogaebeomcikdbafleihmjmbnmanokfbdkibhabdmdgbencabfikhnccjeceiolggbahnhcjgbnhojkkmgbmgddajmicdafgklkkdogaebeomcikdbafleihmjmbnmanokfbdkibhabdmdgbencabfikhnccjeceiolggbahnhcjgbnhojkkmgbmgddajmicdafgklkkdogaebeomcikdbafleihmjmbnmanokfbdkibhabdmdgbencabfikhnccjeceiolggbahnhcjgbnhojkkmgbmgddajmicdafgklkkdogaebeomcikdbafleihmjmbnmanokfbdkibhabdmdgbencabfikhnccjeceiolggbahnhcjgbnhojkkmgbmgddajmicdafgklkkdogaebeomcikdbafleihmjmbnmanokfbdkibhabdmdgbencabfikhnccjeceiolggbahnhcjgbnhojkkmgbmgddajmicdafgklkkdogaebeomcikdbafleihmjmbnmanokfbdkibhabdmdgbencabfikhnccjeceiolggbahnhcjgbnhojkkmgbmgddajmicdafgklkkdogaebeomcikdbafleihmjmbnmanokfbdkibhabdmdgbencabfikhnccjeceiolggbahnh", s2 = "gkcjamihkljkhonhcbableadmjfhofaomcfhgbifmendjhcgbgcejbnddijhbjjfmogjkamngcaodjknebfdnmdblikckcbicdejgkcjamihkljkhonhcbableadmjfhofaomcfhgbifmendjhcgbgcejbnddijhbjjfmogjkamngcaodjknebfdnmdblikckcbicdejgkcjamihkljkhonhcbableadmjfhofaomcfhgbifmendjhcgbgcejbnddijhbjjfmogjkamngcaodjknebfdnmdblikckcbicdejgkcjamihkljkhonhcbableadmjfhofaomcfhgbifmendjhcgbgcejbnddijhbjjfmogjkamngcaodjknebfdnmdblikckcbicdejgkcjamihkljkhonhcbableadmjfhofaomcfhgbifmendjhcgbgcejbnddijhbjjfmogjkamngcaodjknebfdnmdblikckcbicdejgkcjamihkljkhonhcbableadmjfhofaomcfhgbifmendjhcgbgcejbnddijhbjjfmogjkamngcaodjknebfdnmdblikckcbicdejgkcjamihkljkhonhcbableadmjfhofaomcfhgbifmendjhcgbgcejbnddijhbjjfmogjkamngcaodjknebfdnmdblikckcbicdejgkcjamihkljkhonhcbableadmjfhofaomcfhgbifmendjhcgbgcejbnddijhbjjfmogjkamngcaodjknebfdnmdblikckcbicdejgkcjamihkljkhonhcbableadmjfhofaomcfhgbifmendjhcgbgcejbnddijhbjjfmogjkamngcaodjknebfdnmdblikckcbicdejgkcjamihkljkhonhcbableadmjfhofaomcfhgbifmendjhcgbgcejbnddijhbjjfmogjkamngcaodjknebfdnmdblikckcbicdej", baseStr = "rcomcrewoankfivfgfcfkgeadtnmhagjczisqblyldidsuhfdsooviilaaosgswjbqzhkwfwdgqbnuypegvsqoborpnhtjjaxcpjwtxowutansksxzzydoottmknysmpxyetwhlghwbwqvsasmwjsdcgzgfudhettrasxayqdtjkykeyxvqzuvwtlfnoyvauiilqtfstoeilmzbncnxildnjaaoxezuflkthcgdjneycktavzmsovdtxpxjtcfxfkyvsfxnzrwdnnjcnkplctexlgqzipfvqcxfawzdznhbhtdkhfoirliqdfehsiviiimntnuzyfhnbgxakhozldclhxjzpgzyabxwrrfalqdfeaxtvkkucslhrypsjexjdhbeuuckolfgrvxecuhslcbezuxsoklmqpmobybqausuneushwgrrtafujsljzpprklapncxlwktpitejlujycahvvfvggrzayolskjvaauocfikptwiyntvqejfdxirsbmqqrilnmcopskbtdlozevmbiaxraspymfnyaxgazfxsuoygeqzoccmsxamtpcquxvrpsqzdqxaaouyjnrmqxlsvfwsfnmeqyvvufkvlzhzpsfqojrdntpxekahrknbrjtzmhrasbynxwnzfoishiaqmomkcgfsokrdmxmjyxrmrsaphcxicbfubzbvaeuevvvsidhgtzhxevtjxwiwriqkomltbaenbgxxdvzdcuddixkudbcoplqvyyzrkkkjxlqilowootcapiygayfpqzlhdfemmweynumqocfjlicesvbziglxvuqrimxbntrpaebvcbvdeqkepgnejlfkynpqzfamfylvogkakhgeuqqiegsvjoxjfgoiadlevwnwdwyljvvdzrzgiryhmepannhyfzvzxxbaxnqfrgnpksxomdojqvquwqagomfjubsrkxmnwdwfixbwmegdljzcjtdonufsoweesjlvjqivx"))