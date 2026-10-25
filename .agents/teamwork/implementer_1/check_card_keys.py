import json
from pathlib import Path

ROOT = Path(r'e:\repository\SvartulfrVerse')
EDITABLE_FIELDS = set([
    'name', 'display_name', 'avatar', 'description', 'personality', 'mes_example',
    'first_mes', 'scenario', 'post_history_instructions', 'pre_history_instructions',
    'visual_description', 'creator_notes', 'model_url', 'soundcloud_url', 'character_note',
    'tagline', 'backgroundURL', 'tags', 'community_tags', 'rating', 'chat_name',
    'pronouns', 'outfits', 'default_outfit', 'shared_info', 'alternate_greetings',
    'secretFields', 'secrets', 'fields', 'commands', 'metadata'
])

SYSTEM_READONLY_KEYS = set([
    'id', '_id', 'created_at', 'updated_at', 'creator', 'visibility', 'status',
    'approval_date', 'visibility_submitted_at', 'last_public_submitted_at',
    'rejection_date', 'approval_comment', 'rejection_comment', 'updated_at_by_user',
    'vanity_slug', 'sprite_set', 'statistics_record', 'entity_statistics',
    'can_fork', 'moderation_hold', 'forked_from', 'linked_world',
    'prompt_assembly', 'first_message_name', 'enable_advanced_greetings',
    'greetings', 'token_count', 'npc_count', 'lorebook_npc_count', 'collaborators',
    'gallery', 'lorebooks', 'personas', 'sprite_sets', 'regex_scripts', 'likes',
    'liked_by_me', 'boosted_by_me', 'lexicon'
])

for fname in ['Erik_Douglas_card.json', 'Logan_Douglas_card.json', 'Malachia_Douglas_Bloodmoon_card.json', 'Noah_Douglas_Bloodmoon_card.json', 'Wulfnic_Bloodmoon_card.json']:
    with open(ROOT / 'FINAL' / fname, 'r', encoding='utf-8') as f:
        card = json.load(f)
    card_keys = set(card.keys())
    unaccounted = card_keys - EDITABLE_FIELDS - SYSTEM_READONLY_KEYS
    print(f"{fname}: unaccounted keys = {unaccounted}")
