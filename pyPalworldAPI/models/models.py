from enum import Enum
from typing import Optional

from pydantic import SerializeAsAny
from sqlalchemy import Column, String
from sqlmodel import JSON, Field, SQLModel


class HealthCheck(SQLModel):
    status: str = "OK"


class ItemPassive(SQLModel):
    PassiveSkill1: str
    PassiveSkill2: str
    PassiveSkill3: str
    PassiveSkill4: str


class Items(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    """Auto incremented database primary key."""
    Name: str = Field(index=True, sa_type=String(50))
    DevName: str = Field(sa_type=String(50))
    Image: Optional[str] = Field(sa_type=String(100))
    Type: str = Field(index=True, sa_type=String(45))
    Rank: int
    MaxStackCount: int
    Weight: float
    Gold: int
    Durability: Optional[int]
    MagazineSize: Optional[int]
    PhysicalAttackValue: Optional[int]
    HPValue: Optional[int]
    PhysicalDefenseValue: Optional[int]
    ShieldValue: Optional[int]
    MagicAttackValue: Optional[int]
    MagicDefenseValue: Optional[int]
    Description: str
    ItemActorClass: Optional[str] = Field(sa_type=String(50))
    PassiveSkills: SerializeAsAny[ItemPassive] = Field(sa_column=Column(JSON))


class Crafting(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    """Auto incremented database primary key."""
    Name: str
    Output: int
    WorkAmount: int
    Material: dict[str, int] = Field(sa_column=Column(JSON))


class Gear(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    """Auto incremented database primary key."""
    Name: str = Field(index=True, sa_type=String(50))
    Common: dict[str, int] = Field(sa_column=Column(JSON))
    Uncommon: dict[str, int] = Field(sa_column=Column(JSON))
    Rare: dict[str, int] = Field(sa_column=Column(JSON))
    Epic: dict[str, int] = Field(sa_column=Column(JSON))
    Legendary: dict[str, int] = Field(sa_column=Column(JSON))


class PalTypes(SQLModel):
    Name: str
    Image: str


class PalSuitability(SQLModel):
    Name: str
    Image: str
    Level: int


class PalAura(SQLModel):
    Name: str
    Description: str
    Tech: Optional[str]


class PalSkills(SQLModel):
    Name: str
    Type: str
    Description: str
    Level: int
    Cooldown: int
    Power: int


class StatsAttack(SQLModel):
    Melee: int
    Ranged: int


class StatsSpeed(SQLModel):
    Walk: int
    Run: int
    Ride: int


class PalStats(SQLModel):
    HP: int
    Attack: SerializeAsAny[StatsAttack]
    Defense: int
    Stamina: int
    Speed: SerializeAsAny[StatsSpeed]
    Support: int
    Food: int
    CraftSpeed: int
    TransportSpeed: int
    EnemyMaxHPRate: float
    EnemyReceiveDamageRate: float
    EnemyInflictDamageRate: float


class PalBreeding(SQLModel):
    Rank: int = Field(description="CombiRank")
    Order: int
    MaleProbability: float = Field(description="MaleProbability")


class PalDrops(SQLModel):
    Name: str
    Rate: float
    Min: int
    Max: int


class Pals(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    """Auto incremented database primary key."""
    DexKey: str = Field(sa_type=String(4), description="ZukanIndex")
    Image: str = Field(sa_type=String(100))
    Name: str = Field(index=True, sa_type=String(50))
    Wiki: str = Field(sa_type=String(100))
    WikiImage: str = Field(sa_type=String(100))
    Types: SerializeAsAny[list[PalTypes]] = Field(sa_column=Column(JSON))
    Suitability: SerializeAsAny[list[PalSuitability]] = Field(sa_column=Column(JSON))
    Drops: SerializeAsAny[list[PalDrops]] = Field(sa_column=Column(JSON))
    Aura: SerializeAsAny[PalAura] = Field(sa_column=Column(JSON))
    Description: str
    Skills: SerializeAsAny[list[PalSkills]] = Field(sa_column=Column(JSON))
    Stats: SerializeAsAny[PalStats] = Field(sa_column=Column(JSON))
    Asset: str = Field(sa_type=String(50), description="BPClass")
    Genus: str = Field(sa_type=String(50), description="GenusCategory")
    Rarity: int
    Price: int
    Size: str = Field(sa_type=String(2), description="EPalSizeType")
    Maps: dict[str, str] = Field(sa_column=Column(JSON))
    Breeding: SerializeAsAny[PalBreeding] = Field(sa_column=Column(JSON))
    AIResponse: str = Field(sa_type=String(20))
    Nocturnal: bool
    Predator: bool
    NooseTrap: bool
    IsRaidBoss: bool


class BossPals(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    """Auto incremented database primary key."""
    DexKey: str = Field(sa_type=String(4), description="ZukanIndex")
    Image: str = Field(sa_type=String(100))
    Name: str = Field(index=True, sa_type=String(50))
    Wiki: str = Field(sa_type=String(100))
    WikiImage: str = Field(sa_type=String(100))
    Types: SerializeAsAny[list[PalTypes]] = Field(sa_column=Column(JSON))
    Suitability: SerializeAsAny[list[PalSuitability]] = Field(sa_column=Column(JSON))
    Drops: SerializeAsAny[list[PalDrops]] = Field(sa_column=Column(JSON))
    Aura: SerializeAsAny[PalAura] = Field(sa_column=Column(JSON))
    Description: str
    Skills: SerializeAsAny[list[PalSkills]] = Field(sa_column=Column(JSON))
    Stats: SerializeAsAny[PalStats] = Field(sa_column=Column(JSON))
    Asset: str = Field(sa_type=String(50), description="BPClass")
    Genus: str = Field(sa_type=String(50), description="GenusCategory")
    Rarity: int
    Price: int
    Size: str = Field(sa_type=String(2), description="EPalSizeType")
    BattleBGM: str = Field(sa_type=String(50), description="Boss battle location.")
    Maps: dict[str, str] = Field(sa_column=Column(JSON))
    AIResponse: str = Field(sa_type=String(20))
    Nocturnal: bool
    Predator: bool
    NooseTrap: bool
    IsRaidBoss: bool


class Breeding(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    """Auto incremented database primary key."""
    Egg: str = Field(index=True, sa_type=String(50))
    P1: str = Field(sa_type=String(50))
    P2: str = Field(sa_type=String(50))


class PassiveSkills(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    """Auto incremented database primary key."""
    Name: str = Field(index=True, sa_type=String(50))
    DevName: str = Field(sa_type=String(50))
    Ability: str = Field(sa_type=String(50))
    Tier: int
    Description: str
    Image: str = Field(sa_type=String(100))


class FoodEffects(SQLModel):
    Name: str
    Value: int
    Interaval: int


class FoodEffect(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    """Auto incremented database primary key."""
    Name: str = Field(index=True, sa_type=String(50))
    EffectTime: int
    Effects: SerializeAsAny[list[FoodEffects]] = Field(sa_column=Column(JSON))


class TechTree(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    """Auto incremented database primary key."""
    Name: str = Field(index=True, sa_type=String(50))
    UnlockBuildObjects: Optional[list] = Field(sa_column=Column(JSON))
    UnlockItemRecipes: Optional[list] = Field(sa_column=Column(JSON))
    Description: str
    Image: str = Field(sa_type=String(100))
    RequireTechnology: Optional[str] = Field(sa_type=String(50))
    IsBossTechnology: bool
    LevelCap: int
    Cost: int


class SickPal(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    """Auto incremented database primary key."""
    Name: str = Field(index=True, sa_type=String(15))
    EffectiveItemRank: int
    WorkSpeed: int
    MoveSpeed: int
    SatietyDecrease: int
    Description: str
    RecoveryProbabilityPercentageInPalBox: int


class BuildMaterial(SQLModel):
    Name: str = Field(sa_type=String(50))
    Amount: int


class BuildObjects(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    """Auto incremented database primary key."""
    MapObjectId: str = Field(sa_type=String(50))
    Name: str = Field(index=True, sa_type=String(50))
    Description: str
    Image: Optional[str] = Field(sa_type=String(100))
    Material: SerializeAsAny[list[BuildMaterial]] = Field(sa_column=Column(JSON))
    Category: str = Field(index=True, sa_type=String(25), description="TypeA")
    RequiredBuildWorkAmount: float
    InstallNeighborThreshold: float
    IsInstallOnlyOnBase: bool
    IsInstallOnlyHubAround: bool


class APIModels(str, Enum):
    pals = "pals"
    bosspals = "bosspals"
    items = "items"
    breeding = "breeding"
    buildobjects = "buildobjects"
    crafting = "crafting"
    foodeffect = "foodeffect"
    gear = "gear"
    sickpal = "sickpal"
    techtree = "techtree"
    passiveskills = "passiveskills"
    npc = "npc"
    elixir = "elixir"


class NPC(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    """Auto incremented database primary key."""
    Name: str = Field(index=True, sa_type=String(50))
    DevName: str = Field(sa_type=String(50))
    Asset: str = Field(sa_type=String(50), description="BPClass")
    Genus: str = Field(sa_type=String(50), description="GenusCategory")
    Weapon: Optional[str] = Field(sa_type=String(50))
    Stats: SerializeAsAny[PalStats] = Field(sa_column=Column(JSON))
    Rarity: int
    Price: int
    Size: str = Field(sa_type=String(2), description="EPalSizeType")
    AIResponse: str = Field(sa_type=String(20))
    NooseTrap: bool
    Suitability: SerializeAsAny[list[PalSuitability]] = Field(sa_column=Column(JSON))
    IsRaidBoss: bool


class Elixir(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    """Auto incremented database primary key."""
    Name: str = Field(index=True, sa_type=String(50))
    Description: str
    DevName: str = Field(sa_type=String(50))
    MaxHP: int
    MaxSP: int
    Power: int
    WorkSpeed: int
    maxInventoryWeight: int


class AutoCompleteModels(str, Enum):
    palname = "palname"
    paldexkey = "paldexkey"
    bossname = "bossname"
    sickness = "sickness"
    passiveskill = "passiveskill"
    itemname = "itemname"
    itemtype = "itemtype"
    crafting = "crafting"
    gear = "gear"
    food = "food"
    tech = "tech"
    buildname = "buildname"
    buildcategory = "buildcategory"
    elixir = "elixir"
    npc = "npc"
