package net.runelite.client.plugins.DMMSlayAntiPk;
import com.google.inject.Provides;
import net.runelite.api.events.NpcDespawned;
import net.runelite.client.eventbus.Subscribe;
import net.runelite.client.plugins.Plugin;
import net.runelite.api.events.PlayerSpawned;
import net.runelite.api.Client;
import javax.inject.Inject;
import lombok.extern.slf4j.Slf4j;
import net.runelite.client.plugins.PluginDescriptor;
import net.runelite.client.config.ConfigManager;
import java.util.*;

import net.runelite.client.plugins.woodcutting.WoodcuttingConfig;
import sun.audio.*;
import java.io.*;
import net.runelite.api.Renderable;
import net.runelite.api.*;
@Slf4j
@PluginDescriptor(
        name="DmmSlayAntiPk",
        description = "This plugin alerts AFK players to the prescense of players and can let you know when kill is done.",
        enabledByDefault = false
)

public class DMMSlayAntiPk extends Plugin {

    @Inject
    private Client client;

    @Inject
    private DmmSlayConfig config;

    @Provides
    DmmSlayConfig getConfig(ConfigManager configManager)
    {
        return configManager.getConfig(DmmSlayConfig.class);
    }
    @Subscribe
    public void onPlayerSpawned(PlayerSpawned event) throws Exception {
        if (config.PlayerAlert()) {
            log.info("OMGAPLAYER!");
            RUNSOUND();
        }

    }

    @Subscribe
    public void onNpcDespawned(NpcDespawned event) throws Exception {
    NPC actor = event.getNpc();
        if (actor.isDead() && config.NpcDeath())
        {
           log.info("NPC DIED");
            DeathSound();
        }

    }
    public  void RUNSOUND()
            throws Exception
    {
        // open the sound file as a Java input stream
        String gongFile = "C:\\Users\\User\\IdeaProjects\\runelite\\runelite-client\\src\\main\\java\\net\\runelite\\client\\plugins\\DMMSlayAntiPk\\RUN.au";
        InputStream in = new FileInputStream(gongFile);

        // create an audiostream from the inputstream
        AudioStream audioStream = new AudioStream(in);

        // play the audio clip with the audioplayer class
        AudioPlayer.player.start(audioStream);
    }
    public  void DeathSound()
    throws Exception{
        String gongFile = "C:\\Users\\User\\IdeaProjects\\runelite\\runelite-client\\src\\main\\java\\net\\runelite\\client\\plugins\\DMMSlayAntiPk\\died.au";
        InputStream in = new FileInputStream(gongFile);

        // create an audiostream from the inputstream
        AudioStream audioStream = new AudioStream(in);

        // play the audio clip with the audioplayer class
        AudioPlayer.player.start(audioStream);
    }
}








