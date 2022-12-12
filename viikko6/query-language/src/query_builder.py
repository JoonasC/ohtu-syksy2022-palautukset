from matchers import All, And, Or, Not, PlaysIn, HasAtLeast, HasFewerThan

class QueryBuilder:
    def __init__(self, *matchers):
        self._matchers = list(matchers)

    def oneOf(self, *matchers):
        self._matchers.append(Or(*list(matchers)))
        return QueryBuilder(*self._matchers)

    def negate(self, matcher):
        self._matchers.append(Not(matcher))
        return QueryBuilder(*self._matchers)

    def playsIn(self, team):
        self._matchers.append(PlaysIn(team))
        return QueryBuilder(*self._matchers)

    def hasAtLeast(self, value, attr):
        self._matchers.append(HasAtLeast(value, attr))
        return QueryBuilder(*self._matchers)

    def hasFewerThan(self, value, attr):
        self._matchers.append(HasFewerThan(value, attr))
        return QueryBuilder(*self._matchers)

    def build(self):
        if len(self._matchers) == 0:
            return All()
        if len(self._matchers) == 1:
            return self._matchers[0]

        return And(*self._matchers)
