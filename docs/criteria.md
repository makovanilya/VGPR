# VGPR Criteria Specification
**Spec version:** VGPR v1.0  
**Last updated:** 2026-05-03

This markdown file defines the exact falsifiable reasoning why a game gets their rating and their additional modifiers. All are answered with YES or NO, it is recommended that you start from p1 and go up to p5.
Each tier is intentionally written with a lowercase "p". 

## Scale Criteria

### p5 
All of the following must be true:
- [ ] Game launches without contacting any publisher/developer server.
- [ ] All content available at time of purchase remains accessible.
- [ ] No features are gated behind dead infrastructure.
- [ ] Game can be installed from a legitimate owned copy without internet.

### p4 
All of the following must be true:
- [ ] Core gameplay loop is fully intact.
- [ ] Some peripheral features are lost (leaderboards, minor online modes etc.).
- [ ] Community tools or fan servers cover meaningful gaps.
- [ ] Game can still be launched without dead server dependency.

### p3 
All of the following must be true:
- [ ] Game is launchable.
- [ ] Core experience is reachable but meaningfully compromised.
- [ ] Significant paid or advertised content is inaccessible (DLCs, skins etc.).
- [ ] No community solution fully restores the experience.

### p2
All of the following must be true:
- [ ] Game technically launches and displays playable content beyond a server connection screen.
- [ ] Core experience is broken or requires workarounds.
- [ ] Essential functions depend on infrastructure that no longer exists.
- [ ] No official or community solution restores playability.

### p1
One or more of the following must be true:
- [ ] Game cannot be launched at all due to dead server dependency.
- [ ] Publisher remotely revoked consumer licenses.
- [ ] Game was made permanently unplayable by deliberate publisher action.
- [ ] No offline, community, or legal workaround exists.

---

## NR
This means the game is Not Rated and can be used as a placeholder games that are pending a rating.

---

## Modifier Criteria

### Preservation Modifiers

**OS: Open Sourced**  
The developer or publisher has officially released the game's source code under any license that permits use and redistribution.  
- Must be an official release by the company, leaks do not qualify.
- Must include enough code to compile and run the game.

**SDK: Dev Toolkit Released**  
Official modding tools, level editors, or development kits released that meaningfully enable community continuation of the game.  
- Must be an official release by the company.
- Must go beyond basic mod support, enable server hosting or significant content creation with it.

**SRV: Server Binaries Released**  
Official dedicated server software released, enabling community hosting of multiplayer infrastructure.  
- Must be an official release by the company.
- Does not require source code, compiled binaries do qualify.

**SP: Sunset Patch Issued**  
Developer issued a patch before or at shutdown that made the game functional without their servers.  
- Must be released before or simultaneously with the initial server shutdown.
- Must restore meaningful offline functionality.

**ON: Online-Oriented**  
Online play is the core design intent of the game, effects scoring ONLY if publishers did not properly handle it.
- Applies to genres such as MMOs, live-service games, battle royales, online-only co-op games.
- Does NOT apply to singleplayer games with optional multiplayer or games with always online DRM bolted on.

**DRM: Always-Online DRM**  
The game requires a persistent internet connection with no gameplay justification, with the requirement rooting from a DRM service.
- Applies when a singleplayer game requires server ping to launch or play.
- Does NOT apply when an online connection is integral to gameplay (use ON).

**DLS: Delisted**  
The game has been removed from all major storefronts and cannot be legally purchased by new players.  
- Partial delisting (removed from some but not all stores) should be noted in the rating card but does not qualify for the full tag.
- Physical copies still being sold secondhand do not prevent this tag.
