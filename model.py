def predict_diabetes(pregnancies=None,
                     glucose=None,
                     blood_pressure=None,
                     skinfold=None,
                     insulin=None,
                     bmi=None,
                     diabetes_pedigree=None,
                     age=None):
    """ Predictor for Diabetes from model/60917d649f67041342004eaf

        Dataset created from a study of diabetes in females 21 years or older and of Pima Indian heritage. 
        Pima Indians are an interesting population to study for diabetes because they have a higher incidence of diabetes than the general U.S. population.
        Source
        Pima Indians Diabetes Data Set[*] 
        Bache, K. & Lichman, M. (2013). UCI Machine Learning Repository[*]. Irvine, CA: University of California, School of Information and Computer Science.
        
        [*]Pima Indians Diabetes Data Set: http://archive.ics.uci.edu/ml/datasets/Pima+Indians+Diabetes
        [*]UCI Machine Learning Repository: http://archive.ics.uci.edu/ml
    """
    if (glucose is None):
        return u'False'
    if (glucose > 143):
        if (glucose > 159):
            if (bmi is None):
                return u'True'
            if (bmi > 29.23):
                if (glucose > 183):
                    return u'True'
                if (glucose <= 183):
                    if (glucose > 182):
                        return u'False'
                    if (glucose <= 182):
                        if (diabetes_pedigree is None):
                            return u'True'
                        if (diabetes_pedigree > 0.35117):
                            if (age is None):
                                return u'True'
                            if (age > 56):
                                if (bmi > 40.1):
                                    return u'False'
                                if (bmi <= 40.1):
                                    return u'True'
                            if (age <= 56):
                                return u'True'
                        if (diabetes_pedigree <= 0.35117):
                            if (age is None):
                                return u'True'
                            if (age > 49):
                                if (bmi > 35.95):
                                    return u'True'
                                if (bmi <= 35.95):
                                    return u'False'
                            if (age <= 49):
                                if (bmi > 33.8):
                                    if (blood_pressure is None):
                                        return u'True'
                                    if (blood_pressure > 80):
                                        return u'True'
                                    if (blood_pressure <= 80):
                                        if (diabetes_pedigree > 0.2995):
                                            return u'True'
                                        if (diabetes_pedigree <= 0.2995):
                                            if (diabetes_pedigree > 0.144):
                                                return u'False'
                                            if (diabetes_pedigree <= 0.144):
                                                return u'True'
                                if (bmi <= 33.8):
                                    return u'True'
            if (bmi <= 29.23):
                if (bmi > 25.85):
                    return u'False'
                if (bmi <= 25.85):
                    if (bmi > 23.1):
                        return u'True'
                    if (bmi <= 23.1):
                        return u'False'
        if (glucose <= 159):
            if (age is None):
                return u'True'
            if (age > 30):
                if (diabetes_pedigree is None):
                    return u'True'
                if (diabetes_pedigree > 0.224):
                    if (age > 42):
                        if (bmi is None):
                            return u'True'
                        if (bmi > 23.5):
                            return u'True'
                        if (bmi <= 23.5):
                            return u'False'
                    if (age <= 42):
                        if (bmi is None):
                            return u'True'
                        if (bmi > 41.2):
                            return u'True'
                        if (bmi <= 41.2):
                            if (diabetes_pedigree > 0.341):
                                if (skinfold is None):
                                    return u'True'
                                if (skinfold > 35):
                                    if (skinfold > 45):
                                        return u'True'
                                    if (skinfold <= 45):
                                        return u'False'
                                if (skinfold <= 35):
                                    return u'True'
                            if (diabetes_pedigree <= 0.341):
                                return u'False'
                if (diabetes_pedigree <= 0.224):
                    if (blood_pressure is None):
                        return u'False'
                    if (blood_pressure > 79):
                        return u'True'
                    if (blood_pressure <= 79):
                        return u'False'
            if (age <= 30):
                if (diabetes_pedigree is None):
                    return u'False'
                if (diabetes_pedigree > 0.4335):
                    return u'False'
                if (diabetes_pedigree <= 0.4335):
                    if (diabetes_pedigree > 0.333):
                        if (skinfold is None):
                            return u'True'
                        if (skinfold > 50):
                            return u'False'
                        if (skinfold <= 50):
                            if (age > 29):
                                return u'False'
                            if (age <= 29):
                                return u'True'
                    if (diabetes_pedigree <= 0.333):
                        if (blood_pressure is None):
                            return u'False'
                        if (blood_pressure > 62):
                            return u'False'
                        if (blood_pressure <= 62):
                            return u'True'
    if (glucose <= 143):
        if (bmi is None):
            return u'False'
        if (bmi > 26.96202):
            if (age is None):
                return u'False'
            if (age > 28):
                if (glucose > 93):
                    if (insulin is None):
                        return u'False'
                    if (insulin > 202):
                        return u'True'
                    if (insulin <= 202):
                        if (age > 54):
                            if (diabetes_pedigree is None):
                                return u'False'
                            if (diabetes_pedigree > 0.714):
                                return u'True'
                            if (diabetes_pedigree <= 0.714):
                                return u'False'
                        if (age <= 54):
                            if (pregnancies is None):
                                return u'False'
                            if (pregnancies > 7):
                                if (diabetes_pedigree is None):
                                    return u'True'
                                if (diabetes_pedigree > 0.5225):
                                    return u'True'
                                if (diabetes_pedigree <= 0.5225):
                                    if (glucose > 103):
                                        if (glucose > 134):
                                            return u'True'
                                        if (glucose <= 134):
                                            if (glucose > 120):
                                                if (bmi > 40.1):
                                                    return u'True'
                                                if (bmi <= 40.1):
                                                    if (glucose > 131):
                                                        if (bmi > 29.95):
                                                            return u'True'
                                                        if (bmi <= 29.95):
                                                            return u'False'
                                                    if (glucose <= 131):
                                                        return u'False'
                                            if (glucose <= 120):
                                                if (skinfold is None):
                                                    return u'True'
                                                if (skinfold > 45):
                                                    return u'False'
                                                if (skinfold <= 45):
                                                    return u'True'
                                    if (glucose <= 103):
                                        return u'False'
                            if (pregnancies <= 7):
                                if (blood_pressure is None):
                                    return u'False'
                                if (blood_pressure > 59):
                                    if (insulin > 142):
                                        if (insulin > 193):
                                            return u'False'
                                        if (insulin <= 193):
                                            if (skinfold is None):
                                                return u'True'
                                            if (skinfold > 16):
                                                return u'True'
                                            if (skinfold <= 16):
                                                return u'False'
                                    if (insulin <= 142):
                                        if (blood_pressure > 96):
                                            return u'True'
                                        if (blood_pressure <= 96):
                                            if (blood_pressure > 89):
                                                return u'False'
                                            if (blood_pressure <= 89):
                                                if (age > 51):
                                                    return u'True'
                                                if (age <= 51):
                                                    if (diabetes_pedigree is None):
                                                        return u'False'
                                                    if (diabetes_pedigree > 0.1505):
                                                        if (blood_pressure > 63):
                                                            if (pregnancies > 5):
                                                                if (blood_pressure > 83):
                                                                    return u'False'
                                                                if (blood_pressure <= 83):
                                                                    if (insulin > 39):
                                                                        if (bmi > 34.35):
                                                                            if (diabetes_pedigree > 0.3215):
                                                                                return u'True'
                                                                            if (diabetes_pedigree <= 0.3215):
                                                                                return u'False'
                                                                        if (bmi <= 34.35):
                                                                            return u'False'
                                                                    if (insulin <= 39):
                                                                        return u'True'
                                                            if (pregnancies <= 5):
                                                                if (age > 30):
                                                                    if (pregnancies > 1):
                                                                        if (bmi > 31.25):
                                                                            if (bmi > 32.95):
                                                                                if (blood_pressure > 69):
                                                                                    if (glucose > 129):
                                                                                        return u'True'
                                                                                    if (glucose <= 129):
                                                                                        return u'False'
                                                                                if (blood_pressure <= 69):
                                                                                    return u'True'
                                                                            if (bmi <= 32.95):
                                                                                return u'True'
                                                                        if (bmi <= 31.25):
                                                                            return u'False'
                                                                    if (pregnancies <= 1):
                                                                        if (diabetes_pedigree > 0.765):
                                                                            if (glucose > 108):
                                                                                return u'True'
                                                                            if (glucose <= 108):
                                                                                return u'False'
                                                                        if (diabetes_pedigree <= 0.765):
                                                                            return u'True'
                                                                if (age <= 30):
                                                                    return u'False'
                                                        if (blood_pressure <= 63):
                                                            return u'True'
                                                    if (diabetes_pedigree <= 0.1505):
                                                        return u'False'
                                if (blood_pressure <= 59):
                                    return u'False'
                if (glucose <= 93):
                    if (bmi > 29.9):
                        return u'False'
                    if (bmi <= 29.9):
                        if (blood_pressure is None):
                            return u'False'
                        if (blood_pressure > 76):
                            return u'False'
                        if (blood_pressure <= 76):
                            if (blood_pressure > 68):
                                return u'True'
                            if (blood_pressure <= 68):
                                return u'False'
            if (age <= 28):
                if (glucose > 124):
                    if (blood_pressure is None):
                        return u'False'
                    if (blood_pressure > 81):
                        return u'False'
                    if (blood_pressure <= 81):
                        if (bmi > 28.8):
                            if (insulin is None):
                                return u'True'
                            if (insulin > 199):
                                return u'False'
                            if (insulin <= 199):
                                if (insulin > 65):
                                    return u'True'
                                if (insulin <= 65):
                                    if (bmi > 32.35):
                                        return u'False'
                                    if (bmi <= 32.35):
                                        return u'True'
                        if (bmi <= 28.8):
                            return u'False'
                if (glucose <= 124):
                    if (bmi > 49.1125):
                        if (bmi > 56.15):
                            return u'False'
                        if (bmi <= 56.15):
                            return u'True'
                    if (bmi <= 49.1125):
                        if (pregnancies is None):
                            return u'False'
                        if (pregnancies > 7):
                            return u'True'
                        if (pregnancies <= 7):
                            if (bmi > 30.66167):
                                if (glucose > 113):
                                    return u'False'
                                if (glucose <= 113):
                                    if (bmi > 45.4):
                                        return u'True'
                                    if (bmi <= 45.4):
                                        if (bmi > 38.3):
                                            return u'False'
                                        if (bmi <= 38.3):
                                            if (bmi > 37.15):
                                                if (diabetes_pedigree is None):
                                                    return u'False'
                                                if (diabetes_pedigree > 0.5005):
                                                    return u'True'
                                                if (diabetes_pedigree <= 0.5005):
                                                    if (bmi > 37.55):
                                                        return u'False'
                                                    if (bmi <= 37.55):
                                                        return u'True'
                                            if (bmi <= 37.15):
                                                if (bmi > 33.65):
                                                    return u'False'
                                                if (bmi <= 33.65):
                                                    if (skinfold is None):
                                                        return u'False'
                                                    if (skinfold > 34):
                                                        return u'True'
                                                    if (skinfold <= 34):
                                                        if (age > 24):
                                                            if (bmi > 32.8):
                                                                return u'True'
                                                            if (bmi <= 32.8):
                                                                if (skinfold > 29):
                                                                    if (bmi > 31.75):
                                                                        return u'False'
                                                                    if (bmi <= 31.75):
                                                                        return u'True'
                                                                if (skinfold <= 29):
                                                                    return u'False'
                                                        if (age <= 24):
                                                            return u'False'
                            if (bmi <= 30.66167):
                                return u'False'
        if (bmi <= 26.96202):
            if (pregnancies is None):
                return u'False'
            if (pregnancies > 2):
                if (bmi > 26.35):
                    if (skinfold is None):
                        return u'False'
                    if (skinfold > 20):
                        return u'True'
                    if (skinfold <= 20):
                        return u'False'
                if (bmi <= 26.35):
                    if (bmi > 23.9):
                        return u'False'
                    if (bmi <= 23.9):
                        if (glucose > 132):
                            return u'True'
                        if (glucose <= 132):
                            if (diabetes_pedigree is None):
                                return u'False'
                            if (diabetes_pedigree > 0.6365):
                                if (blood_pressure is None):
                                    return u'False'
                                if (blood_pressure > 67):
                                    return u'False'
                                if (blood_pressure <= 67):
                                    return u'True'
                            if (diabetes_pedigree <= 0.6365):
                                return u'False'
            if (pregnancies <= 2):
                return u'False'
