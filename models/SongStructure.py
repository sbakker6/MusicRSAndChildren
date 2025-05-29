from dataclasses import dataclass
from models.Section import Section

@dataclass
class SongStructure:
    @dataclass
    class SectionDescriptor:
        amount : int
        pos_avg : float
        pos_std : float
    
        def __repr__(self):
            return f"amt: {self.amount}, pos_avg: {self.pos_avg}, pos_std: {self.pos_std}"
        
    sections : list[Section] # for example ["Intro", "Pre-Chorus", "Chorus", ...]
    failed : list[str] # any failures are recorded here
    descriptors : dict[Section, SectionDescriptor] 

    def __repr__(self):
        res =  f"{[s.value for s in self.sections]}"
        for s in set(self.sections):
            res += "\n" + f"{s.value} : {self.descriptors[s]}"
        return res

