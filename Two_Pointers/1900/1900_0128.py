class Solution:
    """
    @param Gene1: a string
    @param Gene2: a string
    @return: return the similarity of two gene fragments
    """

    def GeneSimilarity(self, Gene1, Gene2):
        same_time, total_time = 0, 0
        index_gene1, index_gene2 = 0, 0

        num_gene1, curt_gene1, next_index_gene1 = self.read_next_gene(index_gene1, Gene1)
        num_gene2, curt_gene2, next_index_gene2 = self.read_next_gene(index_gene2, Gene2)

        # 因为长度都一样，所以这里选择记录1的num_gene
        total_time += num_gene1
        while curt_gene1 != "" and curt_gene2 != "":
            # 如果相同 gene_char，记录
            if curt_gene1 == curt_gene2:
                same_time += min(num_gene1, num_gene2)

            # 检查哪一个少，指针按照少的那个移动（比如一个为2一个为3，那小的换下一组，多的移动2，-2）
            if num_gene1 < num_gene2:
                num_gene2 -= num_gene1
                num_gene1, curt_gene1, next_index_gene1 = self.read_next_gene(next_index_gene1, Gene1)
                # gene1 一重新提取 total记录
                total_time += num_gene1

            elif num_gene1 > num_gene2:
                num_gene1 -= num_gene2
                num_gene2, curt_gene2, next_index_gene2 = self.read_next_gene(next_index_gene2, Gene2)

            else:
                num_gene1, curt_gene1, next_index_gene1 = self.read_next_gene(next_index_gene1, Gene1)
                num_gene2, curt_gene2, next_index_gene2 = self.read_next_gene(next_index_gene2, Gene2)
                # gene1 一重新提取 total记录
                total_time += num_gene1

        return str(same_time) + "/" + str(total_time)

    def read_next_gene(self, start_index, gene):
        # start_index 到头了
        if start_index >= len(gene):
            return 0, "", start_index
        # 寻找下一个index
        num_gene, gene_char, next_index = "", "", start_index
        while gene_char == "":
            # 当前是数字，则加入（如果数字是好几位的话。10, 100, 所以要一直count)
            if gene[next_index].isdigit():
                num_gene += gene[next_index]
            # 不是数字了
            else:
                gene_char = gene[next_index]
            # index count往前
            next_index += 1
        return int(num_gene), gene_char, next_index

