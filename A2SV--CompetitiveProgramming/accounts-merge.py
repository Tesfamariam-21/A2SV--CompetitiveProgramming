class Solution:
    def findRepresentative(self, representative, x):
        if x == representative[x]:
            return x
        representative[x] = self.findRepresentative(representative, representative[x])  # Path compression
        return representative[x]

    def unionBySize(self, representative, size, a, b):
        representativeA = self.findRepresentative(representative, a)
        representativeB = self.findRepresentative(representative, b)

        if representativeA == representativeB:
            return

        if size[representativeA] >= size[representativeB]:
            size[representativeA] += size[representativeB]
            representative[representativeB] = representativeA
        else:
            size[representativeB] += size[representativeA]
            representative[representativeA] = representativeB

    def accountsMerge(self, accountList):
        accountListSize = len(accountList)
        representative = [i for i in range(accountListSize)]
        size = [1] * accountListSize
        emailGroup = {}

        for i in range(accountListSize):
            accountSize = len(accountList[i])

            for j in range(1, accountSize):
                email = accountList[i][j]
                accountName = accountList[i][0]

                if email not in emailGroup:
                    emailGroup[email] = i
                else:
                    self.unionBySize(representative, size, i, emailGroup[email])

        components = {}
        for email, group in emailGroup.items():
            groupRep = self.findRepresentative(representative, group)

            if groupRep not in components:
                components[groupRep] = []

            components[groupRep].append(email)

        mergedAccounts = []
        for group, component in components.items():
            component.sort()
            component.insert(0, accountList[group][0])
            mergedAccounts.append(component)

        return mergedAccounts
