package net.runelite.client.plugins.DMMSlayAntiPk;
import net.runelite.client.config.Config;
import net.runelite.client.config.ConfigGroup;
import net.runelite.client.config.ConfigItem;
import net.runelite.client.config.Units;
@ConfigGroup("DMMSlayAntiPk")
public interface DmmSlayConfig extends Config{
    @ConfigItem(
            position = 1,
            keyName = "Make Run Alert",
            name = "Player Alert",
            description = "Configures whether to alert you to other players or not"
    )
    default boolean PlayerAlert()
    {
        return true;
    }
    @ConfigItem(
            position = 2,
            keyName = "Make Npc death alert",
            name = "Npc Death alert",
            description = "Configures whether to alert you to npc death or not"
    )
    default boolean NpcDeath()
    {
        return true;
    }

}
