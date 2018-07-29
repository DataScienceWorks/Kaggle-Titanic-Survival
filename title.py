
def title(name):
    titles = ['Mr.','Mrs.','Miss.', 'Ms.', 'Master.', 'Major.', 'Mme.', 
              'Mlle.', 'Sir.', 'Lady.', 'Dr.', 'Rev.', 'Col.', 'Capt.', 'Don.', 'Dona.',
             'Countess.', 'Jonkheer.']
    for t in titles:
        if (t in name):
            return t
