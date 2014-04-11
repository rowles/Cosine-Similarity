__author__ = 'andrew'


import math

people = []
reviews = []
movies = []


# cosine similarity

class Movie:

    def __init__(self, name):
        self.name = name
        movies.append(self)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Review:

    def __init__(self, p, m, r):
        self.person = p;
        self.movie = m;
        self.rating = r;
        reviews.append(self)

    def __str__(self):
        return self.person + ' ' + self.movie + ' ' + self.rating

    def __repr__(self):
        # = ("%s")self.person + ' ' + self.movie + ' ' + self.rating
        return "%s %s %s" % (self.person, self.movie, self.rating)


class Person:

    def __init__(self, name):
        self.name = name
        people.append(self)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def all_reviews(self):
        rs = []
        for r in reviews:
            if r.person == self:
                rs.append(r)
        return rs


def getSim (a_r, b_r):
    # get all similar
    for i in a_r:
        f = False

        for j in b_r:
            if i.movie == j.movie:
                f = True

        if not f:
            a_r.remove(i)
    return a_r

def compare(a, b):
    print a.name
    a_r = []
    b_r = []

    a_r += a.all_reviews()
    b_r += b.all_reviews()

    print "A ", a_r
    print "B ", b_r

    a_r = getSim(a_r, b_r)
    b_r = getSim(b_r, a_r)

    print "A ", a_r
    print "B ", b_r

    # dot product
    d = 0
    for i in range(len(a_r)):
        d += a_r[i].rating*b_r[i].rating

    # length of A vector
    h = 0
    for i in a_r:
        h += i.rating*i.rating
    h = math.sqrt(h)

    # length of B vector
    k = 0
    for j in b_r:
        k += j.rating*j.rating
    k = math.sqrt(k)

    print 'd', d
    print 'h', h
    print 'k', k

    return d / (h*k)


Movie("Wolf of Wall Street"), Movie("Iron Sky"), Movie("Hunger Games")
Person("Andrew")
Review(people[0], movies[0], 5), Review(people[0], movies[1], 3), Review(people[0], movies[2], 2)

Person("Emma")
Review(people[1], movies[0], 4), Review(people[1], movies[1], 3), Review(people[1], movies[2], 4)


print compare(people[0], people[1]);