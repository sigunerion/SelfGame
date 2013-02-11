# -*- coding: utf-8 -*-

def InputDigitList(digitlist):    
    digit = 0    
    while(len(digitlist) <= 10):
        digit = raw_input("数字を入力してください。")
        if digit == "":
            break                
        digitlist.append(int(digit))
    return digitlist

def RemoveFiveMultiple(digitlist):    
    for digit in digitlist:
        if digit % 5 == 0:
            digitlist.remove(digit)    
    return digitlist

def IsRemoveFiveMultiple(digitlist):    
    ModsCount = 0
    for digit in digitlist:
        if digit % 5 == 0:
                ModsCount += 1
    return ModsCount != 0

def IsAllRemoveFiveMultiple(digitlist):    
    ModsCount = 0
    for digit in digitlist:
        if digit % 5 == 0:
                ModsCount += 1
    return ModsCount == len(digitlist)


def HalfNumber(digitlist):
    DisplacementDigitList = []
    for digit in digitlist:
        DisplacementDigitList.append(digit / 2)    
    return DisplacementDigitList    

def CreateDigitList(digitlist):
    newdigitlist =[]
    for digit in digitlist:
        newdigitlist.append(digit)
    return newdigitlist

def CountStep(digitlist,step):    
    step += 1    
    if IsAllRemoveFiveMultiple(digitlist):
        return step
    print digitlist    
    
    HalfDigitList = HalfNumber(digitlist)
    StepHalf = CountStep(HalfDigitList,step)
        
    if IsRemoveFiveMultiple(digitlist):
        ModDigitList = RemoveFiveMultiple(digitlist)
        StepMods = CountStep(ModDigitList,step)
        if StepMods > StepHalf:
            return StepHalf
        else:   
            return StepMods
        
    return StepHalf            

if __name__ == "__main__":
    
    DigitList = []
    DigitList = InputDigitList(DigitList)

    Step = 0

    Step = CountStep(DigitList,Step)
    print Step
    
    
        
        
    