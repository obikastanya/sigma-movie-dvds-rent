class ParameterValidation:
    def cantBeEmpty(parameter):
        for value in parameter.values():
            if not value:
                return False
        return True    
    
    def certainKeyShouldExist(keys, parameter):
        for key in keys:
            if not parameter.get(key):
                return False
        return True

    def atLeastOneNotEmpty(parameter):
        for value in parameter.values():
            if value:
                return True
        return False    
    