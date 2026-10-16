"""Módulo de limpieza: transforma datos crudos en datos usables."""
import pandas as pd
import logging

logger = logging.getLogger('pipeline.limpieza')


def merge_posts_usuarios(posts: pd.DataFrame, usuarios: pd.DataFrame) -> pd.DataFrame:
    """Combina posts con información del autor."""
    logger.info(f"Combinando {len(posts)} posts con {len(usuarios)} usuarios...")
    df = posts.merge(usuarios, on='user_id', how='left')
    sin_autor = df['autor_nombre'].isnull().sum()
    if sin_autor > 0:
        logger.warning(f"{sin_autor} posts sin autor asociado")
    return df
