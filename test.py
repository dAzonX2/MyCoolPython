from dataclasses import dataclass
from dataclasses import field
from dataclasses import InitVar
import pandas as pd
import random
import math
import randominfo as rn_pers

@dataclass
class DataClass_Modern(object):

    attr0:InitVar[int] = 81

    attr1:int   =0
    attr2:str ='undefined'
    attr3:str   ='undefined'
    attr4:list  = field(default_factory=list)

    attr5:float = field(init=False)

    @property
    def attr5(self)->float:
        return math.sqrt(abs(self._attrHidden))

    @attr5.setter
    def attr5(self,_):pass 

    def __post_init__(self,attr0):
        self._attrHidden = attr0
    @classmethod

    def rand_factory(cls):
        '''
        Returns an object of the calling class with randomized initialization attributess
        '''
        return cls(
            attr0=random.randint(0,1e3),
            attr1=random.randint(0,1e6),
            attr2=rn_pers.get_birthdate(startAge = None, endAge = None, _format = '%d %b, %Y'),
            attr3=rn_pers.get_full_name(gender = None),
            attr4=random.choices(rn_pers.get_hobbies(),k=3)
        )

if __name__ == '__main__':

    rand_objects = [DataClass_Modern.rand_factory() for _ in range(100)]
    df = pd.DataFrame(rand_objects)

    print(df)