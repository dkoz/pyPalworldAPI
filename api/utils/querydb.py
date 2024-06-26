from fastapi_pagination.ext.sqlmodel import paginate
from sqlalchemy.sql.expression import text
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from models.models import (
    NPC,
    BossPals,
    Breeding,
    BuidObjects,
    Crafting,
    Elixir,
    FoodEffect,
    Gear,
    Items,
    Pals,
    PassiveSkills,
    SickPal,
    TechTree,
)


async def get_pals(db: AsyncSession, params):
    palstocolume = {
        "name": Pals.Name,
        "dexkey": Pals.DexKey,
        "nocturnal": Pals.Nocturnal,
    }
    wheres = select(Pals)
    for parm in params:
        if parm == "size" or parm == "page":
            continue
        if parm == "nocturnal":
            if params[parm] == "True":
                p = 1
            else:
                p = 0
        else:
            p = params[parm]
        if parm == "type":
            wheres = wheres.where(
                text(
                    "JSON_SEARCH(Types, 'one', :name COLLATE utf8mb4_general_ci)"
                ).bindparams(name=p)
            )
        elif parm == "suitability":
            wheres = wheres.where(
                text(
                    "JSON_SEARCH(Suitability, 'one', :suit COLLATE utf8mb4_general_ci)"
                ).bindparams(suit=p)
            )
        elif parm == "drop":
            wheres = wheres.where(
                text(
                    f"JSON_SEARCH(Drops, 'one', :drop COLLATE utf8mb4_general_ci)"
                ).bindparams(drop=p)
            )
        elif parm == "skill":
            wheres = wheres.where(
                text(
                    "JSON_SEARCH(Skills, 'one', :skill COLLATE utf8mb4_general_ci)"
                ).bindparams(skill=p)
            )
        else:
            wheres = wheres.where(palstocolume[parm] == p)
    return await paginate(db, wheres)


async def get_bosspal(db: AsyncSession, params):
    palstocolume = {
        "name": BossPals.Name,
        "nocturnal": BossPals.Nocturnal,
    }
    wheres = select(BossPals)
    for parm in params:
        if parm == "size" or parm == "page":
            continue
        if parm == "nocturnal":
            if params[parm] == "True":
                p = 1
            else:
                p = 0
        else:
            p = params[parm]
        if parm == "type":
            wheres = wheres.where(
                text(
                    "JSON_SEARCH(Types, 'one', :name COLLATE utf8mb4_general_ci)"
                ).bindparams(name=p)
            )
        elif parm == "suitability":
            wheres = wheres.where(
                text(
                    "JSON_SEARCH(Suitability, 'one', :suit COLLATE utf8mb4_general_ci)"
                ).bindparams(suit=p)
            )
        elif parm == "drop":
            wheres = wheres.where(
                text(
                    f"JSON_SEARCH(Drops, 'one', :drop COLLATE utf8mb4_general_ci)"
                ).bindparams(drop=p)
            )
        elif parm == "skill":
            wheres = wheres.where(
                text(
                    "JSON_SEARCH(Skills, 'one', :skill COLLATE utf8mb4_general_ci)"
                ).bindparams(skill=p)
            )
        else:
            wheres = wheres.where(palstocolume[parm] == p)
    return await paginate(db, wheres)


async def get_item(db: AsyncSession, params):
    itemtocolume = {
        "name": Items.Name,
        "type": Items.Type,
    }
    wheres = select(Items)
    for parm in params:
        if parm == "size" or parm == "page":
            continue
        wheres = wheres.where(itemtocolume[parm] == params[parm])
    return await paginate(db, wheres)


async def get_crafting(db: AsyncSession, name: str):
    return await paginate(db, select(Crafting).where(Crafting.Name == name))


async def get_gear(db: AsyncSession, name: str):
    return await paginate(db, select(Gear).where(Gear.Name == name))


async def get_foodeffects(db: AsyncSession, name: str):
    return await paginate(db, select(FoodEffect).where(FoodEffect.Name == name))


async def get_breeding(db: AsyncSession, name: str):
    return await paginate(db, select(Breeding).where(Breeding.Egg == name))


async def get_sickness(db: AsyncSession, name: str):
    return await paginate(db, select(SickPal).where(SickPal.Name == name))


async def get_tech(db: AsyncSession, name: str):
    return await paginate(db, select(TechTree).where(TechTree.Name == name))


async def get_tech_by_level(db: AsyncSession, level: int):
    return await paginate(db, select(TechTree).where(TechTree.LevelCap == level))


async def get_build(db: AsyncSession, name: str):
    return await paginate(db, select(BuidObjects).where(BuidObjects.Name == name))


async def get_build_by_category(db: AsyncSession, category: str):
    return await paginate(
        db, select(BuidObjects).where(BuidObjects.Category == category)
    )


async def get_passive(db: AsyncSession, name: str):
    return await paginate(db, select(PassiveSkills).where(PassiveSkills.Name == name))


async def get_npc(db: AsyncSession, name: str):
    return await paginate(db, select(NPC).where(NPC.Name == name))


async def get_elixir(db: AsyncSession, name: str):
    return await paginate(db, select(Elixir).where(Elixir.Name == name))


async def get_all(db: AsyncSession, name):
    if name == "pals":
        return await paginate(db, select(Pals))
    elif name == "bosspals":
        return await paginate(db, select(BossPals))
    elif name == "items":
        return await paginate(db, select(Items))
    elif name == "breeding":
        return await paginate(db, select(Breeding))
    elif name == "buidobjects":
        return await paginate(db, select(BuidObjects))
    elif name == "crafting":
        return await paginate(db, select(Crafting))
    elif name == "foodeffect":
        return await paginate(db, select(FoodEffect))
    elif name == "gear":
        return await paginate(db, select(Gear))
    elif name == "sickpal":
        return await paginate(db, select(SickPal))
    elif name == "techtree":
        return await paginate(db, select(TechTree))
    elif name == "passiveskills":
        return await paginate(db, select(PassiveSkills))
    elif name == "npc":
        return await paginate(db, select(NPC))
    elif name == "elixir":
        return await paginate(db, select(Elixir))
    return