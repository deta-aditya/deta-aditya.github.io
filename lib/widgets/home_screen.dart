import 'package:flutter/material.dart';

import 'hero_section.dart';
import 'navigation_button.dart';
import 'skills_section.dart';

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        elevation: 0,
        actions: [
          NavigationButton(
            title: "Skills",
          ),
          NavigationButton(
            title: "Experience",
          ),
          NavigationButton(
            title: "Education",
          ),
          NavigationButton(
            title: "Accomplishments",
          ),
          NavigationButton(
            title: "Contact",
          ),
        ],
      ),
      body: ListView(
        children: [
          HeroSection(),
          SkillsSection(),
        ],
      ),
    );
  }
}







