"""
Custom License — August 8, 2025
Copyright (c) 2025 TheHolyOneZ


This license applies to:
- All files in this project directory and its subdirectories, including but not limited to all Python (*.py) files.
- All versions and components of the "ordersystem", including any file containing code, logic, or functionality originally created by TheHolyOneZ, whether in whole or in part.


Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated files (the “Software”), to use the Software only under the following conditions:

The Software may be run/executed.

Emojis in the Software’s interface may be changed.

No other modifications are allowed without prior written permission from the copyright holder.

The name of the Software, any usernames, or any branding (including but not limited to “TheHolyOneZ”, “TheZ”, and “ZygnalBot”) may not be changed.

The Software may not be transferred, redistributed, sublicensed, sold, or given to any third party.

No code snippets, components, or portions of the Software may be extracted for use in other projects.

The Software may not be copied, reproduced, or made publicly accessible except by the copyright holder.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

License Agreement (By Running it)
Issued to: TheHolyOneZ
Date: 08 August 2025

1. Definitions
This License Agreement (hereinafter the “License”) governs the use of the software/bot created by TheHolyOneZ (hereinafter the “Author”).

2. Permitted Actions
a) The Licensee may run/execute the bot.
b) The Licensee may change emojis in the bot’s interface.
c) No other functional or structural changes are allowed without the Author’s prior written consent.

3. Prohibited Actions
Without the Author’s prior written permission, the Licensee may not:
a) Change the bot’s name, username, project name, or any branding/labels associated with the software — including (but not limited to) “TheHolyOneZ”, “TheZ”, or “ZygnalBot”.
b) Transfer, resell, gift, sublicense, or otherwise distribute the bot to any third party.
c) Extract code snippets, segments, or entire portions of the software for use in other projects, repositories, or products.
d) Copy, reproduce, or make the bot publicly accessible in any form.

4. Ownership and Copyright
All rights, including copyright and all related intellectual property rights, remain solely with the Author TheHolyOneZ.

5. Disclaimer and Warranty
The software is provided “as is” without any warranty of any kind, express or implied. The Author shall not be liable for any damages, including but not limited to loss of profit, data loss, or other indirect damages arising from the use of the software.

6. Term and Termination
This License takes effect on the above date and remains valid until revoked in writing by the Author.
If the Licensee violates Section 3, this License terminates immediately, and the Licensee must delete the software and destroy all copies.

7. Governing Law and Jurisdiction
Where legally permissible, this License is governed by the laws of Germany. The place of jurisdiction shall be the Author’s location.

8. Miscellaneous
Any amendments or additions to this License require written form and the explicit consent of the Author.
"""



import discord
from discord.ext import commands, tasks
from discord import app_commands, ui
from discord.app_commands import AppCommandError
from discord.errors import NotFound
import sqlite3
import json
import os
import random
import string
import datetime
import asyncio
import psutil
import platform
import reportlab
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
import io
import sys
import aiofiles
import re

license_text = """
Custom License — August 8, 2025
Copyright (c) 2025 TheHolyOneZ

This license applies to:
- All files in this project directory and its subdirectories, including but not limited to all Python (*.py) files.
- All versions and components of the "ordersystem", including any file containing code, logic, or functionality originally created by TheHolyOneZ, whether in whole or in part.



Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated files (the “Software”), to use the Software only under the following conditions:

The Software may be run/executed.

Emojis in the Software’s interface may be changed.

No other modifications are allowed without prior written permission from the copyright holder.

The name of the Software, any usernames, or any branding (including but not limited to “TheHolyOneZ”, “TheZ”, and “ZygnalBot”) may not be changed.

The Software may not be transferred, redistributed, sublicensed, sold, or given to any third party.

No code snippets, components, or portions of the Software may be extracted for use in other projects.

The Software may not be copied, reproduced, or made publicly accessible except by the copyright holder.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

License Agreement (By Running it)
Issued to: TheHolyOneZ
Date: 08 August 2025

1. Definitions
This License Agreement (hereinafter the “License”) governs the use of the software/bot created by TheHolyOneZ (hereinafter the “Author”).

2. Permitted Actions
a) The Licensee may run/execute the bot.
b) The Licensee may change emojis in the bot’s interface.
c) No other functional or structural changes are allowed without the Author’s prior written consent.

3. Prohibited Actions
Without the Author’s prior written permission, the Licensee may not:
a) Change the bot’s name, username, project name, or any branding/labels associated with the software — including (but not limited to) “TheHolyOneZ”, “TheZ”, or “ZygnalBot”.
b) Transfer, resell, gift, sublicense, or otherwise distribute the bot to any third party.
c) Extract code snippets, segments, or entire portions of the software for use in other projects, repositories, or products.
d) Copy, reproduce, or make the bot publicly accessible in any form.

4. Ownership and Copyright
All rights, including copyright and all related intellectual property rights, remain solely with the Author TheHolyOneZ.

5. Disclaimer and Warranty
The software is provided “as is” without any warranty of any kind, express or implied. The Author shall not be liable for any damages, including but not limited to loss of profit, data loss, or other indirect damages arising from the use of the software.

6. Term and Termination
This License takes effect on the above date and remains valid until revoked in writing by the Author.
If the Licensee violates Section 3, this License terminates immediately, and the Licensee must delete the software and destroy all copies.

7. Governing Law and Jurisdiction
Where legally permissible, this License is governed by the laws of Germany. The place of jurisdiction shall be the Author’s location.

8. Miscellaneous
Any amendments or additions to this License require written form and the explicit consent of the Author.
"""

NEW_IMAGE_URL = "https://images-ext-1.discordapp.net/external/3yvcKom21ZpS0T0-kpN5e5--k6-Tegqlyipj77rrmJE/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1401993060140712017/a4caa9dc0c42370acc7230003b462a54.png"

print(license_text)

class Tee(object):
    def __init__(self, *files):
        self.files = files
    def write(self, obj):
        for f in self.files:
            f.write(obj)
            f.flush()
    def flush(self, *args, **kwargs):
        for f in self.files:
            f.flush()

SETUP_DB_NAME = "setup_config.db"
ORDER_TICKETS_DB_NAME = "order_tickets.db"
TAGS_DB_NAME = "tags.db"
PRODUCTS_DB_NAME = "products.db"
DISCOUNTS_DB_NAME = "discounts.db"
STATUSES_DB_NAME = "statuses.db"


def validate_emoji(emoji_string):
    
    if not emoji_string:
        return False

    custom_emoji_pattern = re.compile(r"<a?:[a-zA-Z0-9_]+:[0-9]+>")

    if len(emoji_string) <= 4:
        return True

    if custom_emoji_pattern.match(emoji_string):
        return True
    return False

def get_status_color(status):
    conn = sqlite3.connect(STATUSES_DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT color FROM statuses WHERE name = ?", (status,))
    db_color = cursor.fetchone()
    conn.close()
    if db_color:
        try:
            return int(db_color[0], 16)
        except (ValueError, TypeError):
            return 0x99AAB5 
    colors = {
        "processing": 0xFEE75C,
        "shipped": 0x57F287,
        "delivered": 0x57F287,
        "cancelled": 0xED4245,
        "failed": 0xED4245,
    }
    return colors.get(status, 0x99AAB5)

def format_status(status):
    conn = sqlite3.connect(STATUSES_DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT emoji FROM statuses WHERE name = ?", (status,))
    db_emoji = cursor.fetchone()
    conn.close()
    if db_emoji and validate_emoji(db_emoji[0]):
        return f"{db_emoji[0]} {status.capitalize()}"
    status_map = {
        "processing": "🔄 In Progress",
        "shipped": "✅ Shipped",
        "delivered": "✅ Delivered",
        "cancelled": "❌ Cancelled",
        "failed": "⚠️ Failed"
    }
    return status_map.get(status, status)

def create_progress_bar(current_status, steps):
    progress_bar = []
    for step in steps:
        if step["status"] == current_status:
            progress_bar.append(f"**→ {step['label']}**")
        elif (current_status == 'shipped' and step['status'] == 'processing') or \
             (current_status == 'delivered' and step['status'] != 'delivered') or \
             (current_status in ['cancelled', 'failed']):
            progress_bar.append(f"✅ {step['label']}")
        else:
            progress_bar.append(f"◽ {step['label']}")
    return "\n".join(progress_bar)

async def create_status_embed(order_data, status):
    conn = sqlite3.connect(STATUSES_DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT emoji FROM statuses WHERE name = ?", (status,))
    db_emoji = cursor.fetchone()
    conn.close()
    
    status_emoji = '❓' 
    if db_emoji and validate_emoji(db_emoji[0]):
        status_emoji = db_emoji[0]
    elif status == 'shipped' or status == 'delivered':
        status_emoji = '✅'
    elif status == 'cancelled':
        status_emoji = '❌'
    elif status == 'failed':
        status_emoji = '⚠️'
    
    description_text = 'Your order is being processed.'
    if status == 'shipped':
        description_text = 'Your order has been shipped!'
    elif status == 'delivered':
        description_text = 'Your order has been delivered!'
    elif status == 'cancelled':
        description_text = 'Your order has been cancelled!'
    elif status == 'failed':
        description_text = 'There was an issue processing your order. Please contact support.'
    
    if isinstance(order_data, dict):
        order_number = order_data["order_number"]
        items_json = order_data["items"]
    else:
        order_number = order_data[2]
        items_json = order_data[3]
    
    try:
        order_items = json.loads(items_json) if items_json else []
    except (json.JSONDecodeError, TypeError):
        order_items = []
    
    items_value = "\n".join([f"• {item['name']} (€{item['price']:.2f})" for item in order_items]) if order_items else "No items"
    
    embed = discord.Embed(
        color=get_status_color(status),
        title=f"{status_emoji} Order Status #{order_number}"
    )
    embed.description = f"**{format_status(status)}**\n{description_text}"
    embed.add_field(
        name="Progress",
        value=create_progress_bar(status, [
            {"status": "processing", "label": "Processing"},
            {"status": "shipped", "label": "Shipped"},
            {"status": "delivered", "label": "Delivered"}
        ]),
        inline=False
    )
    embed.add_field(
        name="Order Details",
        value=items_value,
        inline=False
    )
    embed.add_field(
        name="Last Update",
        value=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        inline=False
    )

    embed.set_thumbnail(url=NEW_IMAGE_URL)

    embed.set_footer(text="For questions, contact our support team", icon_url=NEW_IMAGE_URL)
    
    return embed

def generate_short_id(length=6):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_pdf_invoice(order_data):
    if isinstance(order_data, dict):
        order_number = order_data["order_number"]
        items_json = order_data["items"]
        subtotal = order_data["subtotal"] or 0
        discount_code = order_data["discount_code"]
        discount_amount = order_data["discount_amount"] or 0
        total_amount = order_data["total_amount"] or 0
    else:
        order_number = order_data[2]
        items_json = order_data[3]
        subtotal = order_data[4] or 0
        discount_code = order_data[5]
        discount_amount = order_data[6] or 0
        total_amount = order_data[7] or 0
        
    file_path = f'./invoice_{order_number}.pdf'
    
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter
    styles = getSampleStyleSheet()

    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width/2.0, height - 50, "Invoice")
    
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 100, f"Order Number: #{order_number}")
    c.drawString(50, height - 120, f"Date: {datetime.date.today().strftime('%Y-%m-%d')}")
    
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 160, "Services:")
    
    y = height - 180
    try:
        items = json.loads(items_json) if items_json else []
    except (json.JSONDecodeError, TypeError):
        items = []
        
    c.setFont("Helvetica", 12)
    for item in items:
        c.drawString(70, y, f"{item['name']}: €{item['price']:.2f}")
        y -= 20
        
    y -= 20
    c.line(50, y, width - 50, y)
    y -= 20
    
    c.setFont("Helvetica-Bold", 12)
    c.drawString(width - 200, y, f"Subtotal: €{subtotal:.2f}")
    y -= 20
    if discount_amount > 0:
        discount_value = subtotal * (discount_amount / 100)
        c.drawString(width - 200, y, f"Discount ({discount_code}): -€{discount_value:.2f}")
        y -= 20
    
    c.drawString(width - 200, y, f"Total: €{total_amount:.2f}")

    c.showPage()
    c.save()
    
    return file_path

def get_payment_instructions(method, order_number, total_amount):
    if method == "paypal":
        return f"Please send **€{total_amount:.2f}** to `**NOt USED**`\n**Memo:** {order_number}"
    elif method == "bank":
        return f"```\nRecipient: Example Company\nIBAN: **NOt USED**\nBIC: **NOt USED**\nAmount: €{total_amount:.2f}\nMemo: {order_number}\n```"
    elif method == "crypto":
        return (f"**Crypto Payment:**\nPlease send the exact amount to one of the following addresses:\n"
                f"**Bitcoin (BTC):** `**NOt USED**`\n"
                f"**Ethereum (ETH):** `**NOt USED**`\n"
                f"**Important:** Your memo is: `{order_number}`")
    else:
        return "Please follow the payment instructions for your selected method."
        
class CreateDiscountModal(ui.Modal, title="Create New Discount Code"):
    def __init__(self, cog):
        super().__init__()
        self.cog = cog
        
        self.code = ui.TextInput(
            label="Discount Code (e.g., SAVE20)",
            placeholder="No spaces or special characters",
            min_length=3,
            max_length=20,
            required=True
        )
        self.add_item(self.code)
        
        self.percent = ui.TextInput(
            label="Discount Percentage (e.g., 20)",
            placeholder="Enter a number between 1-100",
            min_length=1,
            max_length=3,
            required=True
        )
        self.add_item(self.percent)

        self.max_uses = ui.TextInput(
            label="Total Times Code Can Be Used (Overall)",
            placeholder="e.g., 50. Leave empty for unlimited.",
            required=False
        )
        self.add_item(self.max_uses)
        
        self.usage_rules = ui.TextInput(
            label="Per-User Rules (e.g., '1' or '2,5')",
            placeholder="1 = Once/User | 2,5 = 5 Times/User",
            required=True
        )
        self.add_item(self.usage_rules)

        self.expires_at = ui.TextInput(
            label="Expiration Date (YYYY-MM-DD)",
            placeholder="e.g., 2025-12-31",
            min_length=10,
            max_length=10,
            required=True
        )
        self.add_item(self.expires_at)
        
    async def on_submit(self, interaction: discord.Interaction):
        await self.cog.handle_create_discount_modal_submit(interaction, self)

class RemoveDiscountModal(ui.Modal, title="Remove Discount Code"):
    def __init__(self, cog):
        super().__init__()
        self.cog = cog
        self.code = ui.TextInput(
            label="Discount Code to Remove",
            min_length=3,
            max_length=20,
            required=True
        )
        self.add_item(self.code)

    async def on_submit(self, interaction: discord.Interaction):
        await self.cog.handle_remove_discount_modal_submit(interaction, self)

class ApplyDiscountModal(ui.Modal, title="Apply Discount Code"):
    def __init__(self, cog):
        super().__init__(timeout=None)
        self.cog = cog
        self.discount_code = ui.TextInput(
            label="Discount Code",
            placeholder="Enter your discount code here",
            min_length=3,
            max_length=20,
            required=True
        )
        self.add_item(self.discount_code)

    async def on_submit(self, interaction: discord.Interaction):
        await self.cog.handle_apply_discount_modal_submit(interaction, self.discount_code.value)

class TicketSelectMenu(ui.Select):
    def __init__(self, bot):
        options = [
            discord.SelectOption(
                label="Support",
                description="For general questions and assistance.",
                emoji="❓",
                value="support"
            ),
            discord.SelectOption(
                label="Purchase",
                description="To order our services.",
                emoji="🛒",
                value="purchase"
            ),
            discord.SelectOption(
                label="Other",
                description="Anything else that doesn't fit the options.",
                emoji="⚙️",
                value="other"
            )
        ]
        super().__init__(placeholder="Make a selection!", custom_id="ticketsystemid", options=options)
        self.bot = bot

    async def callback(self, interaction: discord.Interaction):
        value = self.values[0]
        cog = interaction.client.get_cog("OrderSystem")
        if not cog:
            await interaction.response.send_message("Cog not found.", ephemeral=True)
            return

        conn_order_tickets = sqlite3.connect(ORDER_TICKETS_DB_NAME)
        conn_order_tickets.row_factory = sqlite3.Row
        cursor_order_tickets = conn_order_tickets.cursor()
        cursor_order_tickets.execute("SELECT * FROM tickets WHERE user_id = ? AND guild_id = ?", (str(interaction.user.id), str(interaction.guild_id)))
        existing_ticket = cursor_order_tickets.fetchone()
        conn_order_tickets.close()
        
        if existing_ticket:
            channel = cog.bot.get_channel(int(existing_ticket["channel_id"]))
            if channel:
                embed = discord.Embed(title="Ticket Already Exists", description=f"You already have an active ticket in this server: {channel.mention}", color=discord.Color.red())
                return await interaction.response.send_message(embed=embed, ephemeral=True)
            else:
                conn_order_tickets = sqlite3.connect(ORDER_TICKETS_DB_NAME)
                cursor_order_tickets = conn_order_tickets.cursor()
                cursor_order_tickets.execute("DELETE FROM tickets WHERE user_id = ? AND guild_id = ?", (str(interaction.user.id), str(interaction.guild_id)))
                conn_order_tickets.commit()
                conn_order_tickets.close()
                await interaction.followup.send("Detected a stale ticket record. Please try creating your ticket again.", ephemeral=True)

        if value == "purchase":
            await interaction.response.defer(ephemeral=True)
            await cog.show_purchase_products(interaction)
        elif value == "other":
            await cog.handle_other_ticket_modal(interaction)
        else:
            await cog.create_ticket(interaction, value)

class ProductSelectMenu(ui.Select):
    def __init__(self, products, bot):
        options = []
        for product in products:
            emoji_to_use = "🛒"
            if product['emoji'] and validate_emoji(product['emoji']):
                emoji_to_use = product['emoji']
            
            options.append(discord.SelectOption(
                label=f"{product['name']} (€{product['price']:.2f})",
                description=product['description'][:100] if product['description'] else "No description",
                emoji=emoji_to_use,
                value=product['product_key']
            ))
        
        super().__init__(placeholder="Select a product to purchase...", custom_id="product_select", options=options)
        self.bot = bot

    async def callback(self, interaction: discord.Interaction):
        selected_product_key = self.values[0]
        cog = interaction.client.get_cog("OrderSystem")
        if cog:
            conn_order_tickets = sqlite3.connect(ORDER_TICKETS_DB_NAME)
            conn_order_tickets.row_factory = sqlite3.Row
            cursor_order_tickets = conn_order_tickets.cursor()
            cursor_order_tickets.execute("SELECT * FROM tickets WHERE user_id = ? AND guild_id = ?", (str(interaction.user.id), str(interaction.guild_id)))
            existing_ticket = cursor_order_tickets.fetchone()
            conn_order_tickets.close()
            
            if existing_ticket:
                channel = cog.bot.get_channel(int(existing_ticket["channel_id"]))
                if channel:
                    embed = discord.Embed(title="Ticket Already Exists", description=f"You already have an active ticket in this server: {channel.mention}", color=discord.Color.orange())
                    return await interaction.response.send_message(embed=embed, ephemeral=True)
                else:
                    conn_order_tickets = sqlite3.connect(ORDER_TICKETS_DB_NAME)
                    cursor_order_tickets = conn_order_tickets.cursor()
                    cursor_order_tickets.execute("DELETE FROM tickets WHERE user_id = ? AND guild_id = ?", (str(interaction.user.id), str(interaction.guild_id)))
                    conn_order_tickets.commit()
                    conn_order_tickets.close()
                    await interaction.followup.send("Detected a stale ticket record. Please try creating your ticket again.", ephemeral=True)
                    return

            await cog.create_purchase_ticket(interaction, selected_product_key)

class ProductSelectView(ui.View):
    def __init__(self, products, bot):
        super().__init__(timeout=300)
        self.add_item(ProductSelectMenu(products, bot))

class TicketView(ui.View):
    def __init__(self, ticket_type, product_key=None):
        super().__init__(timeout=None)
        self.ticket_type = ticket_type
        self.product_key = product_key
        
        close_button = ui.Button(custom_id="close", label="Close", emoji="❌", style=discord.ButtonStyle.secondary)
        claim_button = ui.Button(custom_id="claim", label="Claim", emoji="✅", style=discord.ButtonStyle.success)
        transcript_button = ui.Button(custom_id="transcript", label="Transcript", emoji="📜", style=discord.ButtonStyle.primary)
        show_supporters_button = ui.Button(custom_id="show_supporters", label="Show Supporters", emoji="👥", style=discord.ButtonStyle.primary)
        
        self.add_item(close_button)
        self.add_item(claim_button)
        self.add_item(transcript_button)
        self.add_item(show_supporters_button)
        
        if self.ticket_type == "purchase":
            discount_button = ui.Button(custom_id="apply_discount", label="Apply Discount", emoji="🎟️", style=discord.ButtonStyle.success)
            self.add_item(discount_button)

    @classmethod
    def from_cog(cls, cog, ticket_type, product_key=None):
        view = cls(ticket_type, product_key)
        view.cog = cog
        return view

class OrderView(ui.View):
    def __init__(self, order_number):
        super().__init__(timeout=None)
        self.order_number = order_number

    @ui.button(custom_id="selectPayment", label="Proceed to Payment", style=discord.ButtonStyle.primary)
    async def select_payment_callback(self, interaction: discord.Interaction, button: ui.Button):
        cog = interaction.client.get_cog("OrderSystem")
        if cog:
            await cog.handle_select_payment(interaction)

    @ui.button(custom_id="add_more", label="Add More Services", style=discord.ButtonStyle.secondary)
    async def add_more_callback(self, interaction: discord.Interaction, button: ui.Button):
        cog = interaction.client.get_cog("OrderSystem")
        if cog:
            await cog.handle_add_more_services(interaction)

    @ui.button(custom_id="apply_discount", label="Apply Discount Code", style=discord.ButtonStyle.success, emoji="🎟️")
    async def apply_discount_callback(self, interaction: discord.Interaction, button: ui.Button):
        cog = interaction.client.get_cog("OrderSystem")
        if cog:
            await cog.handle_apply_discount_modal(interaction)

    @ui.button(custom_id="remove_discount", label="Remove Discount", style=discord.ButtonStyle.danger, emoji="❌")
    async def remove_discount_callback(self, interaction: discord.Interaction, button: ui.Button):
        cog = interaction.client.get_cog("OrderSystem")
        if cog:
            await cog.handle_remove_discount(interaction)

class OrderConfirmView(ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @ui.button(custom_id="final_confirm", label="Confirm Order", style=discord.ButtonStyle.success)
    async def final_confirm_callback(self, interaction: discord.Interaction, button: ui.Button):
        cog = interaction.client.get_cog("OrderSystem")
        if cog:
            await cog.handle_final_confirm(interaction)

    @ui.button(custom_id="cancel_order", label="Cancel", style=discord.ButtonStyle.danger)
    async def cancel_order_callback(self, interaction: discord.Interaction, button: ui.Button):
        await interaction.response.send_message("Order has been cancelled.", ephemeral=True)

class OrderCompleteView(ui.View):
    def __init__(self, has_reviews_channel):
        super().__init__(timeout=None)
        self.has_reviews_channel = has_reviews_channel

        self.add_item(ui.Button(custom_id="generate_invoice", label="Download Invoice", style=discord.ButtonStyle.secondary))
        self.add_item(ui.Button(custom_id="check_status", label="Order Status", style=discord.ButtonStyle.primary))
        if self.has_reviews_channel:
            self.add_item(ui.Button(custom_id="rate_service", label="Rate Service", style=discord.ButtonStyle.success, emoji="⭐"))

class CancelConfirmView(ui.View):
    def __init__(self, timeout=60):
        super().__init__(timeout=timeout)
        self.value = False

    @ui.button(custom_id="confirm_cancel", label="Yes, Cancel", style=discord.ButtonStyle.danger)
    async def confirm_cancel_callback(self, interaction: discord.Interaction, button: ui.Button):
        self.value = True
        self.stop()
        await interaction.response.send_message("Cancellation confirmed.", ephemeral=True)

    @ui.button(custom_id="cancel_cancel", label="Go Back", style=discord.ButtonStyle.secondary)
    async def cancel_cancel_callback(self, interaction: discord.Interaction, button: ui.Button):
        self.value = False
        self.stop()
        await interaction.response.send_message("Cancellation aborted.", ephemeral=True)

class RatingView(ui.View):
    def __init__(self, order_number):
        super().__init__(timeout=None)
        self.order_number = order_number
        for star in range(1, 6):
            self.add_item(ui.Button(custom_id=f"rate_{star}_{self.order_number}", label=f"{star} ★", style=discord.ButtonStyle.secondary))

class OrderSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.conn_setup = sqlite3.connect(SETUP_DB_NAME)
        self.conn_setup.row_factory = sqlite3.Row
        self.cursor_setup = self.conn_setup.cursor()

        self.conn_order_tickets = sqlite3.connect(ORDER_TICKETS_DB_NAME)
        self.conn_order_tickets.row_factory = sqlite3.Row
        self.cursor_order_tickets = self.conn_order_tickets.cursor()

        self.conn_tags = sqlite3.connect(TAGS_DB_NAME)
        self.conn_tags.row_factory = sqlite3.Row
        self.cursor_tags = self.conn_tags.cursor()

        self.conn_products = sqlite3.connect(PRODUCTS_DB_NAME)
        self.conn_products.row_factory = sqlite3.Row
        self.cursor_products = self.conn_products.cursor()

        self.conn_discounts = sqlite3.connect(DISCOUNTS_DB_NAME)
        self.conn_discounts.row_factory = sqlite3.Row
        self.cursor_discounts = self.conn_discounts.cursor()

        self.conn_statuses = sqlite3.connect(STATUSES_DB_NAME)
        self.conn_statuses.row_factory = sqlite3.Row
        self.cursor_statuses = self.conn_statuses.cursor()

        self.status_message_cache = {}
        self.last_cpu_usage = psutil.cpu_times()
        self.last_measure_time = datetime.datetime.now().timestamp()
        self.log_file_pointer = 0
        
        self.setup_database()
        self.initialize_default_products()
        self.initialize_default_statuses()

    def setup_database(self):
        print("Initializing databases...")

        conn_setup = sqlite3.connect(SETUP_DB_NAME)
        conn_setup.row_factory = sqlite3.Row
        cursor_setup = conn_setup.cursor()
        cursor_setup.execute("""
            CREATE TABLE IF NOT EXISTS setup (
                guild_id TEXT PRIMARY KEY,
                channel_id TEXT,
                staff_role_id TEXT,
                support_category_id TEXT,
                purchase_category_id TEXT,
                other_category_id TEXT,
                transcript_channel_id TEXT,
                reviews_channel_id TEXT,
                supporter_role_ids TEXT,
                status_channel_id TEXT
            )
        """)
        cursor_setup.execute("PRAGMA table_info(setup)")
        columns = [column[1] for column in cursor_setup.fetchall()]
        if 'debug_channel_id' not in columns:
            cursor_setup.execute("ALTER TABLE setup ADD COLUMN debug_channel_id TEXT")
        if 'debug_interval' not in columns:
            cursor_setup.execute("ALTER TABLE setup ADD COLUMN debug_interval INTEGER")
        conn_setup.commit()
        conn_setup.close()
        print(f"Database '{SETUP_DB_NAME}' initialized.")


        conn_order_tickets = sqlite3.connect(ORDER_TICKETS_DB_NAME)
        conn_order_tickets.row_factory = sqlite3.Row
        cursor_order_tickets = conn_order_tickets.cursor()
        cursor_order_tickets.execute("PRAGMA table_info(tickets)")
        columns = [column[1] for column in cursor_order_tickets.fetchall()]
        required_ticket_columns = ['ticket_message_id', 'order_number', 'guild_id']
        schema_needs_update = not all(col in columns for col in required_ticket_columns)
        if schema_needs_update:
            print(f"Detected outdated 'tickets' table schema in '{ORDER_TICKETS_DB_NAME}'. Dropping and recreating 'tickets' table.")
            cursor_order_tickets.execute("DROP TABLE IF EXISTS tickets")
        cursor_order_tickets.execute("""
            CREATE TABLE IF NOT EXISTS tickets (
                username TEXT,
                user_id TEXT,
                tickets_count INTEGER,
                channel_id TEXT,
                ticket_message_id TEXT DEFAULT NULL,
                ticket_type TEXT,
                product_key TEXT DEFAULT NULL,
                order_number TEXT DEFAULT NULL,
                claimed_by_id TEXT DEFAULT NULL,
                guild_id TEXT DEFAULT NULL,
                UNIQUE(user_id, guild_id)
            )
        """)
        cursor_order_tickets.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                order_number TEXT UNIQUE,
                items TEXT,
                status TEXT DEFAULT 'processing',
                subtotal REAL,
                discount_code TEXT,
                discount_amount REAL DEFAULT 0,
                total_amount REAL,
                payment_method TEXT,
                created_at TEXT,
                updated_at TEXT,
                tag TEXT DEFAULT NULL
            )
        """)
        cursor_order_tickets.execute("PRAGMA table_info(orders)")
        columns = [column[1] for column in cursor_order_tickets.fetchall()]
        if 'guild_id' not in columns:
            cursor_order_tickets.execute("ALTER TABLE orders ADD COLUMN guild_id TEXT")
            print("LOG: Added 'guild_id' column to 'orders' table.")
        cursor_order_tickets.execute("""
            CREATE TABLE IF NOT EXISTS payments (
                payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                order_id INTEGER,
                order_number TEXT,
                method TEXT,
                amount REAL,
                status TEXT DEFAULT 'pending',
                created_at TEXT,
                FOREIGN KEY (order_id) REFERENCES orders (order_id)
            )
        """)
        cursor_order_tickets.execute("""
            CREATE TABLE IF NOT EXISTS tracking (
                tracking_id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id INTEGER,
                order_number TEXT UNIQUE,
                status TEXT DEFAULT 'processing',
                channel_id TEXT,
                status_message_id TEXT,
                ticket_message_id TEXT,
                history TEXT,
                created_at TEXT,
                updated_at TEXT,
                FOREIGN KEY (order_id) REFERENCES orders (order_id)
            )
        """)
        conn_order_tickets.commit()
        conn_order_tickets.close()
        print(f"Database '{ORDER_TICKETS_DB_NAME}' initialized.")
        

        conn_tags = sqlite3.connect(TAGS_DB_NAME)
        conn_tags.row_factory = sqlite3.Row
        cursor_tags = conn_tags.cursor()
        cursor_tags.execute("PRAGMA table_info(order_tag_functions)")
        columns = {column[1]: column[2] for column in cursor_tags.fetchall()}
        if 'functions' not in columns or columns.get('functions') != 'TEXT' or \
           'status_change' not in columns or columns.get('status_change') != 'TEXT':
            print("Detected outdated 'order_tag_functions' table schema. Dropping and recreating table.")
            cursor_tags.execute("DROP TABLE IF EXISTS order_tag_functions")
            cursor_tags.execute("""
                CREATE TABLE IF NOT EXISTS order_tag_functions (
                    tag_name TEXT PRIMARY KEY,
                    functions TEXT,
                    status_change TEXT
                )
            """)
        else:
             print(f"Database '{TAGS_DB_NAME}' schema is up to date.")
        cursor_tags.execute("""
            CREATE TABLE IF NOT EXISTS order_tags_channels (
                tag_name TEXT PRIMARY KEY,
                channel_id TEXT NOT NULL
            )
        """)
        conn_tags.commit()
        conn_tags.close()
        print(f"Database '{TAGS_DB_NAME}' initialized.")


        conn_products = sqlite3.connect(PRODUCTS_DB_NAME)
        conn_products.row_factory = sqlite3.Row
        cursor_products = conn_products.cursor()
        cursor_products.execute("""
            CREATE TABLE IF NOT EXISTS products (
                product_key TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                description TEXT,
                emoji TEXT,
                embed_title TEXT,
                embed_description TEXT,
                embed_color INTEGER DEFAULT 5865474,
                has_instructions BOOLEAN DEFAULT 0,
                instruction_embed_title TEXT,
                instruction_embed_description TEXT,
                instruction_embed_color INTEGER DEFAULT 5865474,
                is_active BOOLEAN DEFAULT 1,
                created_at TEXT,
                updated_at TEXT
            )
        """)
        conn_products.commit()
        conn_products.close()
        print(f"Database '{PRODUCTS_DB_NAME}' initialized.")


        conn_discounts = sqlite3.connect(DISCOUNTS_DB_NAME)
        conn_discounts.row_factory = sqlite3.Row
        cursor_discounts = conn_discounts.cursor()


        cursor_discounts.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='discounts'"
        )
        table_exists = cursor_discounts.fetchone() is not None

        if table_exists:

            cursor_discounts.execute("PRAGMA table_info(discounts)")
            columns = [column[1] for column in cursor_discounts.fetchall()]

            if ('reusable' in columns or
                'usage_type' not in columns or
                'max_uses_per_user' not in columns):
                print("LOG: Updating 'discounts' table schema for new usage rules.")
                cursor_discounts.execute("ALTER TABLE discounts RENAME TO discounts_old")
                cursor_discounts.execute("""
                    CREATE TABLE discounts (
                        code TEXT PRIMARY KEY,
                        percent INTEGER,
                        expires_at TEXT,
                        created_at TEXT,
                        created_by TEXT,
                        is_active BOOLEAN DEFAULT 1,
                        max_uses INTEGER, 
                        used_count INTEGER DEFAULT 0,
                        usage_type TEXT DEFAULT 'single',
                        max_uses_per_user INTEGER,
                        description TEXT,
                        applies_to TEXT
                    )
                """)
                try:
                    cursor_discounts.execute("""
                        INSERT INTO discounts (
                            code, percent, expires_at, created_at, created_by,
                            is_active, max_uses, used_count, usage_type,
                            max_uses_per_user, description, applies_to
                        )
                        SELECT
                            code, percent, expires_at, created_at, created_by,
                            is_active, max_uses, used_count,
                            CASE
                                WHEN reusable = 1 THEN 'multiple'
                                ELSE 'single'
                            END AS usage_type,
                            NULL AS max_uses_per_user,
                            description, applies_to
                        FROM discounts_old
                    """)
                    cursor_discounts.execute("DROP TABLE discounts_old")
                    print("LOG: Successfully migrated data to new 'discounts' schema.")
                except sqlite3.Error as e:
                    print(f"WARNING: Could not migrate old discount data, starting fresh. Error: {e}")
            else:
                print("LOG: 'discounts' table schema is up to date.")
        else:
            print("LOG: 'discounts' table not found, creating new one.")
            cursor_discounts.execute("""
                CREATE TABLE discounts (
                    code TEXT PRIMARY KEY,
                    percent INTEGER,
                    expires_at TEXT,
                    created_at TEXT,
                    created_by TEXT,
                    is_active BOOLEAN DEFAULT 1,
                    max_uses INTEGER, 
                    used_count INTEGER DEFAULT 0,
                    usage_type TEXT DEFAULT 'single',
                    max_uses_per_user INTEGER,
                    description TEXT,
                    applies_to TEXT
                )
            """)


        cursor_discounts.execute("""
            CREATE TABLE IF NOT EXISTS discount_usage (
                usage_id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_number TEXT,
                user_id TEXT,
                discount_code TEXT,
                used_at TEXT
            )
        """)
        conn_discounts.commit()
        conn_discounts.close()
        print(f"Database '{DISCOUNTS_DB_NAME}' initialized.")



        conn_statuses = sqlite3.connect(STATUSES_DB_NAME)
        conn_statuses.row_factory = sqlite3.Row
        cursor_statuses = conn_statuses.cursor()
        cursor_statuses.execute("""
            CREATE TABLE IF NOT EXISTS statuses (
                name TEXT PRIMARY KEY,
                emoji TEXT NOT NULL,
                color TEXT NOT NULL
            )
        """)
        conn_statuses.commit()
        conn_statuses.close()
        print("All databases initialized successfully.")

    def initialize_default_products(self):
        print("Initializing default products...")
        default_products = [
            {
                "product_key": "server_creation",
                "name": "Custom Server Creation",
                "price": 50.00,
                "description": "A new Discord server created to your specifications.",
                "emoji": "🛠️",
                "embed_title": "Custom Server Creation - €50.00",
                "embed_description": "**What's Included:**\n• Complete server setup\n• Custom roles and permissions\n• Channel structure design\n• Bot integration\n• Custom emojis and branding\n\n**Delivery Time:** 1-3 business days",
                "embed_color": 0x5865F2,
                "has_instructions": True,
                "instruction_embed_title": "📋 Setup Instructions",
                "instruction_embed_description": "**To get started with your custom server:**\n\n1. **Server Theme:** Tell us what type of server you want (Gaming, Community, Business, etc.)\n2. **Color Scheme:** Preferred colors for roles and embeds\n3. **Channel Structure:** List the channels you need\n4. **Special Features:** Any bots or special permissions needed\n5. **Branding:** Upload any logos or images you want included\n\nPlease provide this information in this ticket and our team will begin working on your server!",
                "instruction_embed_color": 0x57F287
            },
            {
                "product_key": "bot_adjustments", 
                "name": "Specialized ZygnalBot Sourcecode Adjustments",
                "price": 30.00,
                "description": "Specialized adjustments to the ZygnalBot sourcecode.",
                "emoji": "💻",
                "embed_title": "ZygnalBot Sourcecode Adjustments - €30.00",
                "embed_description": "**What's Included:**\n• Custom command creation\n• Feature modifications\n• Bug fixes and optimizations\n• Database adjustments\n• Custom integrations\n\n**Delivery Time:** 2-5 business days",
                "embed_color": 0x5865F2,
                "has_instructions": True,
                "instruction_embed_title": "⚙️ Development Instructions",
                "instruction_embed_description": "**For your bot adjustments:**\n\n1. **Current Issue:** Describe what needs to be fixed or changed\n2. **Desired Outcome:** Explain what you want the bot to do\n3. **Code Access:** Provide repository access or code files\n4. **Testing Environment:** Share your test server invite\n5. **Priority Features:** List most important changes first\n\nOur developers will review your requirements and provide an implementation timeline!",
                "instruction_embed_color": 0x57F287
            }
        ]
        for product in default_products:
            self.cursor_products.execute("SELECT product_key FROM products WHERE product_key = ?", (product["product_key"],))
            if not self.cursor_products.fetchone():
                self.cursor_products.execute("""
                    INSERT INTO products (
                        product_key, name, price, description, emoji, embed_title, 
                        embed_description, embed_color, has_instructions, 
                        instruction_embed_title, instruction_embed_description, 
                        instruction_embed_color, created_at, updated_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    product["product_key"], product["name"], product["price"], 
                    product["description"], product["emoji"], product["embed_title"],
                    product["embed_description"], product["embed_color"], 
                    product["has_instructions"], product.get("instruction_embed_title"),
                    product.get("instruction_embed_description"), 
                    product.get("instruction_embed_color", 0x57F287),
                    datetime.datetime.now().isoformat(), datetime.datetime.now().isoformat()
                ))
                print(f"LOG: Inserted default product: {product['name']}")
            else:
                print(f"LOG: Product '{product['name']}' already exists, skipping insertion.")
        self.conn_products.commit()
        print("Default products initialization complete.")

    def initialize_default_statuses(self):
        print("Initializing default statuses...")
        default_statuses = [
            {"name": "processing", "emoji": "🔄", "color": "FEE75C"},
            {"name": "shipped", "emoji": "✅", "color": "57F287"},
            {"name": "delivered", "emoji": "✅", "color": "57F287"},
            {"name": "cancelled", "emoji": "❌", "color": "ED4245"},
            {"name": "failed", "emoji": "⚠️", "color": "ED4245"},
        ]
        
        for status in default_statuses:
            self.cursor_statuses.execute("SELECT name FROM statuses WHERE name = ?", (status["name"],))
            if not self.cursor_statuses.fetchone():
                self.cursor_statuses.execute("""
                    INSERT INTO statuses (name, emoji, color) VALUES (?, ?, ?)
                """, (status["name"], status["emoji"], status["color"]))
                print(f"LOG: Inserted default status: {status['name']}")
            else:
                print(f"LOG: Status '{status['name']}' already exists, skipping insertion.")
        self.conn_statuses.commit()
        print("Default statuses initialization complete.")

    def cog_unload(self):
        print("Unloading cog and closing database connections...")
        self.conn_setup.close()
        self.conn_order_tickets.close()
        self.conn_tags.close()
        self.conn_products.close()
        self.conn_discounts.close()
        self.conn_statuses.close()
        if hasattr(self, 'update_status_task'):
            self.update_status_task.cancel()
        if hasattr(self, 'payment_reminder_task'):
            self.payment_reminder_task.cancel()
        if hasattr(self, 'debug_log_task'):
            self.debug_log_task.cancel()
        print("Database connections closed.")

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Logged in as {self.bot.user}!")
        
        self.update_status_task.start()
        self.payment_reminder_task.start()
        
        try:
            await self.bot.tree.sync()
            print("Successfully synchronized slash commands globally.")
        except Exception as e:
            print(f"Failed to synchronize slash commands: {e}")
        try:
            self.cursor_setup.execute("SELECT debug_channel_id, debug_interval FROM setup")
            debug_config = self.cursor_setup.fetchone()
            if debug_config and debug_config["debug_channel_id"] and debug_config["debug_interval"]:
                self.debug_log_task.change_interval(seconds=debug_config["debug_interval"])
                self.debug_log_task.start()
                print(f"LOG: Restarted debug log task with interval {debug_config['debug_interval']} seconds.")
        except Exception as e:
            print(f"Error starting debug log task on ready: {e}")
        print("Attempting to re-attach views to active tickets...")
        self.cursor_order_tickets.execute("SELECT channel_id, ticket_message_id, ticket_type, product_key FROM tickets")
        active_tickets = self.cursor_order_tickets.fetchall()
        for ticket in active_tickets:
            channel_id = int(ticket["channel_id"])
            message_id = int(ticket["ticket_message_id"]) if ticket["ticket_message_id"] else None
            ticket_type = ticket["ticket_type"]
            product_key = ticket["product_key"]
            if not message_id:
                print(f"LOG: Skipping ticket in channel {channel_id}: No ticket_message_id found.")
                continue
            try:
                channel = self.bot.get_channel(channel_id)
                if not channel:
                    print(f"LOG: Channel {channel_id} not found for ticket. Deleting stale record from '{ORDER_TICKETS_DB_NAME}'.")
                    self.cursor_order_tickets.execute("DELETE FROM tickets WHERE channel_id = ?", (str(channel_id),))
                    self.conn_order_tickets.commit()
                    continue
                message = await channel.fetch_message(message_id)
                if ticket_type == "purchase":
                    view = TicketView.from_cog(self, ticket_type, product_key)
                else:
                    view = TicketView.from_cog(self, ticket_type)
                await message.edit(view=view)
                print(f"LOG: Successfully re-attached view to ticket in channel {channel.name} (Message ID: {message_id}).")
            except NotFound:
                print(f"ERROR: Message {message_id} not found in channel {channel_id} for ticket. Deleting stale record from '{ORDER_TICKETS_DB_NAME}'.")
                self.cursor_order_tickets.execute("DELETE FROM tickets WHERE channel_id = ?", (str(channel_id),))
                self.conn_order_tickets.commit()
            except Exception as e:
                print(f"ERROR: Error re-attaching view for ticket in channel {channel_id}: {e}")
        print("Finished re-attaching views.")
        print(license_text)


    @tasks.loop(minutes=2)
    async def update_status_task(self):
        self.cursor_setup.execute("SELECT status_channel_id FROM setup")
        row = self.cursor_setup.fetchone()
        if not row or not row["status_channel_id"]:
            print("LOG: Status channel not configured, skipping status update task.")
            return
            
        status_channel_id = row["status_channel_id"]
        channel = self.bot.get_channel(int(status_channel_id))
        if not channel:
            print(f"ERROR: Status channel {status_channel_id} not found.")
            return
            
        try:
            metrics = await self.gather_metrics()
            embed = self.create_status_embed_for_ping(metrics)
            messages = [m async for m in channel.history(limit=1)]
            if messages and messages[0].author == self.bot.user:
                await messages[0].edit(embed=embed)
                print(f"LOG: Updated existing status message in {channel.name}.")
            else:
                await channel.send(embed=embed)
                print(f"LOG: Sent new status message in {channel.name}.")
        except Exception as e:
            print(f"ERROR: Failed to send status update: {e}")

    @tasks.loop(hours=24)
    async def payment_reminder_task(self):
        print("LOG: Running payment reminder task...")
        two_days_ago = (datetime.datetime.now() - datetime.timedelta(days=2)).isoformat()
        
        self.cursor_order_tickets.execute("SELECT * FROM payments WHERE status = 'pending' AND created_at < ?", (two_days_ago,))
        pending_payments = self.cursor_order_tickets.fetchall()
        
        for payment in pending_payments:
            try:
                user = await self.bot.fetch_user(payment["user_id"])
                embed = discord.Embed(
                    color=0xED4245,
                    title="⏰ Payment Reminder"
                ).add_field(
                    name="Details",
                    value=f"You have a pending payment of **€{payment['amount']:.2f}** for order **#{payment['order_number']}**."
                ).set_footer(text="Please complete your payment to avoid cancellation.")
                await user.send(embed=embed)
                print(f"LOG: Sent payment reminder to user {user.id} for order {payment['order_number']}.")
            except NotFound:
                print(f"ERROR: User with ID {payment['user_id']} not found for payment reminder.")
            except Exception as e:
                print(f"ERROR: Failed to send payment reminder to user {payment['user_id']}: {e}")
        print("LOG: Payment reminder task completed.")

    @tasks.loop(seconds=60)
    async def debug_log_task(self):
        self.cursor_setup.execute("SELECT debug_channel_id FROM setup")
        config = self.cursor_setup.fetchone()
        
        if not config or not config["debug_channel_id"]:
            print("LOG: Debug channel not configured, stopping debug log task.")
            self.debug_log_task.stop()
            return

        channel = self.bot.get_channel(int(config["debug_channel_id"]))
        if not channel:
            print(f"ERROR: Debug channel {config['debug_channel_id']} not found.")
            return

        try:
            log_file_size = os.path.getsize("logs/bot.log")
            
            if log_file_size > self.log_file_pointer:
                async with aiofiles.open("logs/bot.log", 'r', encoding='utf-8', errors='ignore') as f:
                    await f.seek(self.log_file_pointer)
                    new_logs = await f.read()
                    self.log_file_pointer = await f.tell()
                    
                if new_logs.strip():
                    for chunk in [new_logs[i:i+1900] for i in range(0, len(new_logs), 1900)]:
                        await channel.send(f"```\n{chunk}\n```")
            else:
                self.log_file_pointer = 0

        except FileNotFoundError:
            await channel.send("❌ Error: Log file not found.")
            self.debug_log_task.stop()
        except Exception as e:
            print(f"ERROR: Failed to send debug logs: {e}")

    @app_commands.command(name="help", description="Shows all available commands and their subcommands.")
    async def help_command(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' requested help commands.")
        
        embed = discord.Embed(
            title="📚 Bot Commands Help",
            description="Here are all available commands and their subcommands:",
            color=0x5865F2
        )
        
        embed.add_field(
            name="🏓 `/status`",
            value=(
                "**Subcommands:**\n"
                "• `show` - Display current system diagnostics\n"
                "• `auto` - Enable/disable automatic status updates in a channel\n"
                "\n**Usage:** `/status show` or `/status auto`"
            ),
            inline=False
        )
        
        embed.add_field(
            name="🎫 `/ticket-config`",
            value=(
                "**Parameters:**\n"
                "• `setup_channel` - Channel where ticket creation message is sent\n"
                "• `staff_role` - Role for staff who can manage tickets\n"
                "• `support_category` - Category for support tickets\n"
                "• `purchase_category` - Category for purchase tickets\n"
                "• `other_category` - Category for other tickets\n"
                "• `transcript_channel` - Channel for ticket transcripts\n"
                "• `reviews_channel` - Channel for customer reviews (optional)\n"
                "• `supporter_roles` - Comma-separated supporter role IDs or Mentions (optional)\n"
                "\n**Usage:** `/ticket-config [all parameters required]`\n"
                "**Permission:** Administrator"
            ),
            inline=False
        )
        
        embed.add_field(
            name="📦 Product Management",
            value=(
                "**`/product-create`** - Create a new product\n"
                "• `product_key` - Unique identifier (no spaces)\n"
                "• `name` - Product name\n"
                "• `price` - Product price\n"
                "• `description` - Product description\n"
                "• `embed_title` - Title for ticket embed\n"
                "• `embed_description` - Description for ticket embed\n"
                "• `emoji` - Product emoji (optional)\n"
                "• `has_instructions` - Show instruction embed (optional)\n"
                "\n**`/product-edit`** - Edit existing product\n"
                "• `product_key` - Product to edit\n"
                "• All other parameters are optional\n"
                "• `embed_color` - Hex color (e.g., 0x5865F2)\n"
                "• `instruction_title` - Instruction embed title\n"
                "• `instruction_description` - Instruction embed description\n"
                "• `instruction_color` - Instruction embed color\n"
                "\n**`/product-remove`** - Remove a product by key\n"
                "• `product_key` - The key of the product to remove\n"
                "\n**`/product-list`** - List all products\n"
                "\n**Permission:** Administrator"
            ),
            inline=False
        )
        
        embed.add_field(
            name="🎟️ `/discounts`",
            value=(
                "**Subcommands:**\n"
                "• `create` - Create new discount code (via a modal)\n"
                "• `remove` - Remove discount code (via a modal)\n"
                "• `list` - List all active discount codes\n"
                "• `usage` - Export a JSON file of all discount code usage.\n"
                "\n**Usage:** `/discounts create`, `/discounts remove`, `/discounts list`, or `/discounts usage`\n"
                "**Permission:** Administrator"
            ),
            inline=False
        )
        
        embed.add_field(
            name="⚙️ Order Tag Commands",
            value=(
                "**`/apply-tag`** - Apply a tag to an order and trigger associated actions\n"
                "**`/set-tag-channel`** - Set the channel for a specific order tag's informational messages\n"
                "**`/create-tag`** - Create a custom tag and link multiple functions to it. New: now includes autocompletion for functions and statuses.\n"
                "**`/list-tags`** - Lists all configured order tags.\n"
                "\n**Available Functions:**\n"
                "• `close_ticket_by_order_id` - Closes the ticket associated with the order ID.\n"
                "• `mark_order_complete` - Sets the order status to 'delivered'.\n"
                "• `mark_order_as_failed` - Sets the order status to 'failed'.\n"
                "• `mark_order_as_shipped` - Sets the order status to 'shipped'.\n"
                "• `send_order_details_to_channel` - Sends a detailed embed about the order to the configured channel for the tag.\n"
                "\n**Permission:** Admin or Staff Role"
            ),
            inline=False
        )
        
        embed.add_field(
            name="⚙️ Other Commands",
            value=(
                "**`/shop`** - Display product catalog for users\n"
                "**`/set-auto-status`** - Sets the channel for automatic status updates.\n"
                "**`/add-status`** - Adds a new order status with an emoji and color.\n"
                "**`/remove-status`** - Removes an existing custom order status.\n"
                "**`/set-debug-logs`** - Sends terminal logs to a specified channel at a set interval.\n"
                "**`/list-orders`** - Lists all active orders.\n"
                "**`/sync`** - Force syncs all slash commands. (Admin only)\n"
                "\n**Permission:** Manage Messages"
            ),
            inline=False
        )
        
        embed.set_footer(text="Use /help to see this help again anytime!")
        embed.timestamp = datetime.datetime.now()
        
        await interaction.followup.send(embed=embed)

    @app_commands.command(name="status", description="System diagnostics with automatic updates.")
    @app_commands.describe(subcommand="Choose a subcommand")
    @app_commands.choices(subcommand=[
        app_commands.Choice(name="show", value="show"),
        app_commands.Choice(name="auto", value="auto")
    ])
    async def status_command(self, interaction: discord.Interaction, subcommand: str):
        if subcommand == "show":
            await self.handle_show_ping(interaction)
        elif subcommand == "auto":
            await self.handle_auto_ping(interaction)

    async def handle_show_ping(self, interaction: discord.Interaction):
        await interaction.response.defer()
        print(f"LOG: '{interaction.user.name}' requested ping show.")
        metrics = await self.gather_metrics()
        embed = self.create_status_embed_for_ping(metrics, interaction.user)
        
        await interaction.followup.send(embed=embed, ephemeral=True)

    async def handle_auto_ping(self, interaction: discord.Interaction, channel: discord.TextChannel = None, status: str = "off"):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' requested ping auto with channel: {channel}, status: {status}.")

        if status == "on" and not channel:
            await interaction.followup.send("Please provide a channel to enable updates.")
            print("ERROR: No channel provided for auto ping 'on' status.")
            return

        self.cursor_setup.execute("UPDATE setup SET status_channel_id = ? WHERE guild_id = ?", (channel.id if status == "on" else None, interaction.guild_id))
        self.conn_setup.commit()
        print(f"LOG: Updated setup DB for guild {interaction.guild.id} with status_channel_id: {channel.id if status == 'on' else 'None'}.")
        if status == "on":
            await interaction.followup.send(f"Automatic updates enabled in {channel.mention} (every 2 minutes).")
            self.update_status_task.restart()
            print("LOG: Automatic updates task restarted.")
        else:
            self.update_status_task.cancel()
            print("LOG: Automatic updates task cancelled.")
            await interaction.followup.send("Automatic updates disabled.")
    
    def create_status_embed_for_ping(self, metrics, user=None):
        embed = discord.Embed(
            title="System Diagnostics",
            color=discord.Color.green()
        )
        embed.add_field(name="Bot Stats", value=f"• Servers: `{metrics['guild_count']}`\n• Users: `{metrics['user_count']}`\n• Uptime: `{metrics['uptime']}`", inline=True)
        embed.add_field(name="Network", value=f"• Latency: `{metrics['ping']}ms`\n• WebSocket: `{metrics['ws_ping']}ms`", inline=True)
        embed.add_field(name="System", value=f"• CPU: `{metrics['cpu_usage']:.2f}%`\n• RAM: `{metrics['memory']['used']:.2f}GB / {metrics['memory']['total']:.2f}GB`", inline=True)
        embed.set_footer(text=f"Requested by {user.name} • PID: {os.getpid()}" if user else f"Automatic update • PID: {os.getpid()}")
        embed.timestamp = datetime.datetime.now()
        return embed

    async def gather_metrics(self):
        cpu_usage = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        boot_time_timestamp = psutil.boot_time()
        uptime_seconds = datetime.datetime.now().timestamp() - boot_time_timestamp
        uptime_string = str(datetime.timedelta(seconds=uptime_seconds)).split('.')[0]
        return {
            'ping': round(self.bot.latency * 1000),
            'ws_ping': round(self.bot.latency * 1000),
            'uptime': uptime_string,
            'guild_count': len(self.bot.guilds),
            'user_count': sum(guild.member_count for guild in self.bot.guilds),
            'cpu_usage': cpu_usage,
            'memory': {
                'total': memory.total / (1024**3),
                'used': memory.used / (1024**3),
                'percent': memory.percent
            }
        }
        
    @app_commands.command(name="ticket-config", description="Set up the ticket system.")
    @app_commands.checks.has_permissions(administrator=True)
    @app_commands.describe(
        setup_channel="The channel where the ticket creation message will be sent.",
        staff_role="The role for staff who can manage tickets.",
        support_category="The category for support tickets.",
        purchase_category="The category for purchase tickets.",
        other_category="The category for other tickets.",
        transcript_channel="The channel where ticket transcripts will be saved.",
        reviews_channel="The channel for customer reviews (optional).",
        supporter_roles="A comma-separated list of supporter roles (IDs or Mentions)."
    )
    async def ticket_config(self, interaction: discord.Interaction,
        setup_channel: discord.TextChannel,
        staff_role: discord.Role,
        support_category: discord.CategoryChannel,
        purchase_category: discord.CategoryChannel,
        other_category: discord.CategoryChannel,
        transcript_channel: discord.TextChannel = None,
        reviews_channel: discord.TextChannel = None,
        supporter_roles: str = ""
        ):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' initiated ticket setup for guild {interaction.guild.id}.")
        try:
            supporter_role_ids = []
            if supporter_roles:
                role_mentions = supporter_roles.split(',')
                for mention in role_mentions:
                    role_id = mention.strip().replace('<@&', '').replace('>', '')
                    if role_id.isdigit():
                        supporter_role_ids.append(role_id)
                    else:
                        print(f"ERROR: Invalid supporter role provided: {mention}")
                        return await interaction.followup.send(f"❌ Invalid supporter role provided: `{mention}`. Please provide a role ID or mention.")
            self.cursor_setup.execute("INSERT OR REPLACE INTO setup (guild_id, channel_id, staff_role_id, support_category_id, purchase_category_id, other_category_id, transcript_channel_id, reviews_channel_id, supporter_role_ids) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (str(interaction.guild_id), str(setup_channel.id), str(staff_role.id), str(support_category.id), str(purchase_category.id), str(other_category.id), str(transcript_channel.id) if transcript_channel else None, str(reviews_channel.id) if reviews_channel else None, json.dumps(supporter_role_ids)))
            self.conn_setup.commit()
            print(f"LOG: Ticket setup configuration saved for guild {interaction.guild.id} in '{SETUP_DB_NAME}'.")
            embed = discord.Embed(
                title="Zygnal Development and Products - Support System",
                description="""
                `Select the option below that suits more the thing you want help with.`
                **Guide to the Ticket System:**
                * **Support Tickets:** For general questions and assistance.
                * **Purchase Tickets:** To order our services.
                * **Other Tickets:** For anything that doesn't fit the other categories.
                Once you select an option, a private channel will be created where you can talk to our staff.
                """,
                color=discord.Color.dark_red()
            )
            view = ui.View(timeout=None)
            view.add_item(TicketSelectMenu(self.bot))
            await setup_channel.send(embed=embed, view=view)
            await interaction.followup.send("Ticket system has been set up!")
            print(f"LOG: Ticket setup message sent to {setup_channel.name}.")
        except Exception as e:
            print(f"ERROR: Error in ticket-config: {e}")
            await interaction.followup.send(f"❌ An error occurred while setting up the ticket system: `{e}`")

    @app_commands.command(name="set-auto-status", description="Sets the channel for automatic status updates.")
    @app_commands.checks.has_permissions(administrator=True)
    @app_commands.describe(
        channel="The channel where the bot will send automatic status updates."
    )
    async def set_auto_status(self, interaction: discord.Interaction, channel: discord.TextChannel):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' setting status channel for guild {interaction.guild.id} to {channel.name}.")
        try:
            self.cursor_setup.execute("UPDATE setup SET status_channel_id = ? WHERE guild_id = ?", (str(channel.id), str(interaction.guild_id)))
            self.conn_setup.commit()
            print(f"LOG: Status channel configured for guild {interaction.guild.id} in '{SETUP_DB_NAME}'.")
            await interaction.followup.send(f"✅ Automatic status updates will now be sent to {channel.mention}.")
        except Exception as e:
            print(f"ERROR: Error in set-auto-status: {e}")
            await interaction.followup.send(f"❌ An error occurred while setting the status channel: `{e}`")
    
    @app_commands.command(name="sync", description="Force syncs all slash commands. (Admin only)")
    @app_commands.checks.has_permissions(administrator=True)
    async def sync_command(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' requested to sync slash commands.")
        try:
            await self.bot.tree.sync()
            await interaction.followup.send("✅ All slash commands have been synced successfully!", ephemeral=True)
            print("LOG: Slash commands synced via /sync-commands.")
        except Exception as e:
            print(f"Failed to sync slash commands: {e}")
            await interaction.followup.send(f"❌ Failed to sync slash commands: `{e}`", ephemeral=True)

    @app_commands.command(name="set-debug-logs", description="Sends terminal logs to a specified channel.")
    @app_commands.checks.has_permissions(administrator=True)
    @app_commands.describe(
        channel="The channel to send the logs to.",
        interval="The interval in seconds to send logs (e.g., 20). Set to 0 to stop."
    )
    async def set_debug_logs(self, interaction: discord.Interaction, channel: discord.TextChannel, interval: int):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' initiated terminal debug log task to channel {channel.name} with interval {interval}s.")
        try:
            if interval <= 0:
                self.debug_log_task.stop()
                self.cursor_setup.execute("UPDATE setup SET debug_channel_id = ?, debug_interval = ? WHERE guild_id = ?", (None, None, str(interaction.guild_id)))
                self.conn_setup.commit()
                print("LOG: Debug log task stopped.")
                await interaction.followup.send("✅ Terminal log printing has been stopped.")
                return
            self.cursor_setup.execute("UPDATE setup SET debug_channel_id = ?, debug_interval = ? WHERE guild_id = ?", (str(channel.id), interval, str(interaction.guild_id)))
            self.conn_setup.commit()
            print(f"LOG: Debug log channel configured for guild {interaction.guild.id} in '{SETUP_DB_NAME}'.")
            if self.debug_log_task.is_running():
                self.debug_log_task.change_interval(seconds=interval)
                print(f"LOG: Debug log task interval changed to {interval}s.")
            else:
                self.debug_log_task.change_interval(seconds=interval)
                self.debug_log_task.start()
                print("LOG: Debug log task started.")
            await interaction.followup.send(f"✅ Terminal logs will be sent to {channel.mention} every `{interval}` seconds.")
        except Exception as e:
            print(f"ERROR: Error in set-debug-logs: {e}")
            await interaction.followup.send(f"❌ An error occurred while setting up the log task: `{e}`")

    @app_commands.command(name="add-status", description="Adds a new custom order status.")
    @app_commands.checks.has_permissions(administrator=True)
    @app_commands.describe(
        name="The name of the status (e.g., 'completed').",
        emoji="An emoji for the status (e.g., '🎉').",
        color="The hex color code for the status (e.g., '00ff00')."
    )
    async def add_status(self, interaction: discord.Interaction, name: str, emoji: str, color: str):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' adding status '{name}'.")
        
        if not validate_emoji(emoji):
            return await interaction.followup.send(f"❌ Invalid emoji provided. Please use a valid unicode or custom emoji format.", ephemeral=True)
            
        try:
            if not color.startswith("0x"):
                color = f"0x{color}"
            int(color, 16)
        except ValueError:
            return await interaction.followup.send(f"❌ Invalid color format: `{color}`. Use a valid hex code without the '0x' prefix.")
        try:
            self.cursor_statuses.execute("INSERT OR REPLACE INTO statuses (name, emoji, color) VALUES (?, ?, ?)", (name.lower(), emoji, color))
            self.conn_statuses.commit()
            print(f"LOG: Status '{name}' added/updated in '{STATUSES_DB_NAME}'.")
            await interaction.followup.send(f"✅ Status `{name}` added/updated successfully with emoji {emoji} and color `{color}`.")
        except Exception as e:
            print(f"ERROR: Error adding status: {e}")
            await interaction.followup.send(f"❌ An error occurred while adding the status: `{e}`")

    @app_commands.command(name="remove-status", description="Removes a custom order status.")
    @app_commands.checks.has_permissions(administrator=True)
    @app_commands.describe(
        name="The name of the status to remove."
    )
    async def remove_status(self, interaction: discord.Interaction, name: str):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' removing status '{name}'.")
        try:
            self.cursor_statuses.execute("DELETE FROM statuses WHERE name = ?", (name.lower(),))
            self.conn_statuses.commit()
            print(f"LOG: Status '{name}' removed from '{STATUSES_DB_NAME}'.")
            await interaction.followup.send(f"✅ Status `{name}` removed successfully.")
        except Exception as e:
            print(f"ERROR: Error removing status: {e}")
            await interaction.followup.send(f"❌ An error occurred while removing the status: `{e}`")
    
    @app_commands.command(name="list-tags", description="Lists all configured order tags.")
    @app_commands.checks.has_permissions(administrator=True)
    async def list_tags(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' requested a list of all tags.")
        try:
            self.cursor_tags.execute("SELECT tag_name, functions, status_change FROM order_tag_functions")
            tags = self.cursor_tags.fetchall()
            if not tags:
                return await interaction.followup.send("❌ No tags have been configured yet.")
            embed = discord.Embed(
                title="🏷️ Configured Order Tags",
                description="Here are all the tags and their associated actions.",
                color=discord.Color.blue()
            )
            for tag in tags:
                functions = json.loads(tag['functions']) if tag['functions'] else "None"
                status = tag['status_change'] if tag['status_change'] else "None"
                functions_str = ", ".join(functions) if functions != "None" else "None"
                embed.add_field(
                    name=f"Tag: `{tag['tag_name']}`",
                    value=f"**Functions:** `{functions_str}`\n**Status Change:** `{status}`",
                    inline=False
                )
            await interaction.followup.send(embed=embed)
            print("LOG: Tag list sent successfully.")
        except Exception as e:
            print(f"ERROR: Error listing tags: {e}")
            await interaction.followup.send(f"❌ An error occurred while listing the tags: `{e}`")

    @app_commands.command(name="product-edit", description="Edit product information and embeds.")
    @app_commands.checks.has_permissions(administrator=True)
    @app_commands.describe(
        product_key="The product key to edit",
        name="New product name",
        price="New product price", 
        description="New product description",
        emoji="New product emoji",
        embed_title="New embed title",
        embed_description="New embed description",
        embed_color="New embed color (hex format: 0x5865F2)",
        has_instructions="Whether this product has instruction embed",
        instruction_title="Instruction embed title",
        instruction_description="New instruction embed description",
        instruction_color="Instruction embed color (hex format: 0x57F287)"
    )
    async def product_edit(self, interaction: discord.Interaction,
        product_key: str,
        name: str = None,
        price: float = None,
        description: str = None,
        emoji: str = None,
        embed_title: str = None,
        embed_description: str = None,
        embed_color: str = None,
        has_instructions: bool = None,
        instruction_title: str = None,
        instruction_description: str = None,
        instruction_color: str = None
        ):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' initiated product edit for key: {product_key}.")
        try:
            self.cursor_products.execute("SELECT * FROM products WHERE product_key = ?", (product_key,))
            product = self.cursor_products.fetchone()
            if not product:
                print(f"ERROR: Product with key '{product_key}' not found for editing.")
                return await interaction.followup.send(f"❌ Product with key `{product_key}` not found!")
            updates = []
            values = []
            if name is not None:
                updates.append("name = ?")
                values.append(name)
            if price is not None:
                updates.append("price = ?")
                values.append(price)
            if description is not None:
                updates.append("description = ?")
                values.append(description)
            if emoji is not None:
                if not validate_emoji(emoji):
                    return await interaction.followup.send("❌ Invalid emoji provided. Please use a valid unicode or custom emoji format.", ephemeral=True)
                updates.append("emoji = ?")
                values.append(emoji)
            if embed_title is not None:
                updates.append("embed_title = ?")
                values.append(embed_title)
            if embed_description is not None:
                updates.append("embed_description = ?")
                values.append(embed_description)
            if embed_color is not None:
                try:
                    color_int = int(embed_color, 16) if embed_color.startswith('0x') else int(embed_color, 16)
                    updates.append("embed_color = ?")
                    values.append(color_int)
                except ValueError:
                    print(f"ERROR: Invalid color format provided: {embed_color}")
                    return await interaction.followup.send(f"❌ Invalid color format: `{embed_color}`. Use format like `0x5865F2`")
            if has_instructions is not None:
                updates.append("has_instructions = ?")
                values.append(has_instructions)
            if instruction_title is not None:
                updates.append("instruction_embed_title = ?")
                values.append(instruction_title)
            if instruction_description is not None:
                updates.append("instruction_embed_description = ?")
                values.append(instruction_description)
            if instruction_color is not None:
                try:
                    color_int = int(instruction_color, 16) if instruction_color.startswith('0x') else int(instruction_color, 16)
                    updates.append("instruction_embed_color = ?")
                    values.append(color_int)
                except ValueError:
                    print(f"ERROR: Invalid instruction color format provided: {instruction_color}")
                    return await interaction.followup.send(f"❌ Invalid instruction color format: `{instruction_color}`. Use format like `0x57F287`")
            if not updates:
                print("LOG: No changes specified for product edit.")
                return await interaction.followup.send("❌ No changes specified!")
            updates.append("updated_at = ?")
            values.append(datetime.datetime.now().isoformat())
            values.append(product_key)
            query = f"UPDATE products SET {', '.join(updates)} WHERE product_key = ?"
            self.cursor_products.execute(query, values)
            self.conn_products.commit()
            print(f"LOG: Product '{product_key}' updated in '{PRODUCTS_DB_NAME}'.")
            self.cursor_products.execute("SELECT * FROM products WHERE product_key = ?", (product_key,))
            updated_product = self.cursor_products.fetchone()
            embed = discord.Embed(
                title="✅ Product Updated Successfully",
                color=0x57F287
            )
            embed.add_field(name="Product Key", value=updated_product["product_key"], inline=True)
            embed.add_field(name="Name", value=updated_product["name"], inline=True)
            embed.add_field(name="Price", value=f"€{updated_product['price']:.2f}", inline=True)
            embed.add_field(name="Description", value=updated_product["description"] or "No description", inline=False)
            embed.add_field(name="Has Instructions", value="Yes" if updated_product["has_instructions"] else "No", inline=True)
            await interaction.followup.send(embed=embed)
            print(f"LOG: Product edit confirmation sent for '{product_key}'.")
        except Exception as e:
            print(f"ERROR: Error in product-edit: {e}")
            await interaction.followup.send(f"❌ An error occurred while editing the product: `{e}`")

    @app_commands.command(name="product-remove", description="Remove a product from the list.")
    @app_commands.checks.has_permissions(administrator=True)
    @app_commands.describe(
        product_key="The product key to remove"
    )
    async def product_remove(self, interaction: discord.Interaction, product_key: str):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' requested product removal for key: {product_key}.")
        try:
            self.cursor_products.execute("SELECT * FROM products WHERE product_key = ?", (product_key,))
            product = self.cursor_products.fetchone()
            if not product:
                print(f"ERROR: Product with key '{product_key}' not found for removal.")
                return await interaction.followup.send(f"❌ Product with key `{product_key}` not found.")
            self.cursor_products.execute("UPDATE products SET is_active = 0 WHERE product_key = ?", (product_key,))
            self.conn_products.commit()
            print(f"LOG: Product '{product_key}' marked as inactive in '{PRODUCTS_DB_NAME}'.")
            await interaction.followup.send(f"✅ Product `{product_key}` has been successfully removed.")
            print(f"LOG: Product removal confirmation sent for '{product_key}'.")
        except Exception as e:
            print(f"ERROR: Error removing product: {e}")
            await interaction.followup.send(f"❌ An error occurred while removing the product: `{e}`")

    @app_commands.command(name="product-list", description="List all available products.")
    @app_commands.checks.has_permissions(administrator=True)
    async def product_list(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' requested product list.")
        try:
            self.cursor_products.execute("SELECT * FROM products WHERE is_active = 1 ORDER BY created_at ASC")
            products = self.cursor_products.fetchall()
            if not products:
                print("LOG: No active products found.")
                return await interaction.followup.send("❌ No products found!")
            embed = discord.Embed(
                title="📦 Product List",
                description="All available products in the system:",
                color=0x5865F2
            )
            for product in products:
                emoji_to_use = "🛒"
                if product['emoji'] and validate_emoji(product['emoji']):
                    emoji_to_use = product['emoji']
                    
                embed.add_field(
                    name=f"{emoji_to_use} {product['name']}",
                    value=(
                        f"**Key:** `{product['product_key']}`\n"
                        f"**Price:** €{product['price']:.2f}\n"
                        f"**Instructions:** {'Yes' if product['has_instructions'] else 'No'}\n"
                        f"**Description:** {(product['description'][:50] + '...') if len(product['description'] or '') > 50 else (product['description'] or 'No description')}"
                    ),
                    inline=True
                )
            await interaction.followup.send(embed=embed)
            print("LOG: Product list sent.")
        except Exception as e:
            print(f"ERROR: Error in product-list: {e}")
            await interaction.followup.send(f"❌ An error occurred while listing products: `{e}`")

    @app_commands.command(name="product-create", description="Create a new product.")
    @app_commands.checks.has_permissions(administrator=True)
    @app_commands.describe(
        product_key="Unique key for the product (no spaces)",
        name="Product name",
        price="Product price",
        description="Product description",
        emoji="Product emoji (optional)",
        embed_title="Embed title for ticket",
        embed_description="Embed description for ticket",
        has_instructions="Whether to show instruction embed (optional)"
    )
    async def product_create(self, interaction: discord.Interaction,
        product_key: str,
        name: str,
        price: float,
        description: str,
        embed_title: str,
        embed_description: str,
        emoji: str = "",
        has_instructions: bool = False
        ):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' initiated product creation for key: {product_key}.")
        try:
            self.cursor_products.execute("SELECT product_key FROM products WHERE product_key = ?", (product_key,))
            if self.cursor_products.fetchone():
                print(f"ERROR: Product with key '{product_key}' already exists.")
                return await interaction.followup.send(f"❌ Product with key `{product_key}` already exists!")
            if not product_key.replace('_', '').isalnum():
                print(f"ERROR: Invalid product key format: {product_key}")
                return await interaction.followup.send("❌ Product key can only contain letters, numbers, and underscores!")

            if emoji and not validate_emoji(emoji):
                return await interaction.followup.send("❌ Invalid emoji provided. Please use a valid unicode or custom emoji format.", ephemeral=True)
            
            self.cursor_products.execute("""
                INSERT INTO products (
                    product_key, name, price, description, emoji, embed_title,
                    embed_description, embed_color, has_instructions, created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                product_key, name, price, description, emoji, embed_title,
                embed_description, 0x5865F2, has_instructions,
                datetime.datetime.now().isoformat(), datetime.datetime.now().isoformat()
            ))
            self.conn_products.commit()
            print(f"LOG: Product '{product_key}' created in '{PRODUCTS_DB_NAME}'.")
            embed = discord.Embed(
                title="✅ Product Created Successfully",
                color=0x57F287
            )
            embed.add_field(name="Product Key", value=product_key, inline=True)
            embed.add_field(name="Name", value=name, inline=True)
            embed.add_field(name="Price", value=f"€{price:.2f}", inline=True)
            embed.add_field(name="Description", value=description, inline=False)
            embed.add_field(name="Has Instructions", value="Yes" if has_instructions else "No", inline=True)
            await interaction.followup.send(embed=embed)
            print(f"LOG: Product creation confirmation sent for '{product_key}'.")
        except Exception as e:
            print(f"ERROR: Error in product-create: {e}")
            await interaction.followup.send(f"❌ An error occurred while creating the product: `{e}`")

    @app_commands.command(name="shop", description="Display a dropdown menu of available products.")
    async def shop_command(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' requested products display.")
        try:
            await self.products_command_logic(interaction)
        except Exception as e:
            print(f"ERROR: Error in products command: {e}")
            await interaction.followup.send(f"❌ An error occurred while fetching products: `{e}`", ephemeral=True)

    async def products_command_logic(self, interaction):
        self.cursor_products.execute("SELECT * FROM products WHERE is_active = 1 ORDER BY price ASC")
        products = self.cursor_products.fetchall()
        if not products:
            print("LOG: No products available to display.")
            return await interaction.followup.send("❌ No products available at the moment.")
        embed = discord.Embed(
            title="**Our Services**",
            description="Pricelist for Zygnal Development and Products | 2025",
            color=discord.Color.green()
        )
        options = []
        for product in products:
            emoji_to_use = "🛒"
            if product['emoji'] and validate_emoji(product['emoji']):
                emoji_to_use = product['emoji']
            
            options.append(discord.SelectOption(
                label=f"{product['name']} (€{product['price']:.2f})",
                description=product['description'][:100] if product['description'] else "No description available",
                emoji=emoji_to_use,
                value=product['product_key']
            ))
        view = ui.View()
        view.add_item(ui.Select(
            custom_id="products_dropdown",
            placeholder="Please select an option",
            options=options
        ))
        if interaction.response.is_done():
            await interaction.followup.send(embed=embed, view=view)
        else:
            await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
        print("LOG: Product catalog displayed.")

    @app_commands.command(name="discounts", description="Manage discount codes.")
    @app_commands.default_permissions(administrator=True)
    @app_commands.describe(subcommand="Choose a subcommand")
    @app_commands.choices(subcommand=[
        app_commands.Choice(name="create", value="create"),
        app_commands.Choice(name="remove", value="remove"),
        app_commands.Choice(name="list", value="list"),
        app_commands.Choice(name="usage", value="usage"),
        app_commands.Choice(name="config", value="config")
    ])
    async def discounts_command(self, interaction: discord.Interaction, subcommand: str):
        print(f"LOG: '{interaction.user.name}' used discount command with subcommand: {subcommand}.")
        if subcommand == "create":
            await self.handle_create_discount(interaction)
        elif subcommand == "remove":
            await self.handle_remove_discount_cmd(interaction)
        elif subcommand == "list":
            await self.handle_list_discounts(interaction)
        elif subcommand == "usage":
            await self.handle_discount_usage(interaction)
        elif subcommand == "config": 

            await interaction.response.send_message("Please use the command `/discount-config` to configure product restrictions.", ephemeral=True)

    async def handle_create_discount(self, interaction: discord.Interaction):
        print(f"LOG: '{interaction.user.name}' opening CreateDiscountModal.")
        await interaction.response.send_modal(CreateDiscountModal(self))

    async def handle_create_discount_modal_submit(self, interaction: discord.Interaction, modal: CreateDiscountModal):
            await interaction.response.defer(ephemeral=True)
            print(f"LOG: '{interaction.user.name}' submitting CreateDiscountModal.")
            try:
                code = modal.code.value.upper()
                percent = int(modal.percent.value)
                expires_at = datetime.datetime.fromisoformat(modal.expires_at.value).isoformat()
                max_uses = int(modal.max_uses.value) if modal.max_uses.value else None
                

                usage_rules_input = modal.usage_rules.value.strip()
                usage_type = None
                max_uses_per_user = None

                if usage_rules_input == "1":
                    usage_type = "single"
                    max_uses_per_user = 1
                elif "," in usage_rules_input:
                    parts = [p.strip() for p in usage_rules_input.split(',')]
                    if len(parts) == 2 and parts[0] == "2" and parts[1].isdigit() and int(parts[1]) > 0:
                        usage_type = "multiple"
                        max_uses_per_user = int(parts[1])
                    else:
                        await interaction.followup.send("❌ Invalid Per-User Rules. For multiple uses, format must be `2,X` where X is a number (e.g., `2,5`).", ephemeral=True)
                        return
                else:
                    await interaction.followup.send("❌ Invalid Per-User Rules. Use `1` for single-use, or `2,X` for multiple uses per user.", ephemeral=True)
                    return


                if not 1 <= percent <= 100:
                    print(f"ERROR: Invalid discount percentage: {percent}.")
                    return await interaction.followup.send("❌ Discount percentage must be between 1 and 100.")
                
                self.cursor_discounts.execute("""
                    INSERT INTO discounts (code, percent, expires_at, created_at, created_by, usage_type, max_uses_per_user, max_uses) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (code, percent, expires_at, datetime.datetime.now().isoformat(), str(interaction.user.id), usage_type, max_uses_per_user, max_uses))
                self.conn_discounts.commit()
                
                print(f"LOG: Discount code '{code}' created and saved to '{DISCOUNTS_DB_NAME}'.")
                embed = discord.Embed(title="✅ Discount Code Created", color=0x57F287)
                embed.add_field(name="Code", value=f"`{code}`", inline=True)
                embed.add_field(name="Percentage", value=f"{percent}%", inline=True)
                embed.add_field(name="Expires", value=modal.expires_at.value, inline=True)
                
                usage_desc = f"One time per user" if usage_type == 'single' else f"{max_uses_per_user} times per user"
                embed.add_field(name="Per-User Limit", value=usage_desc, inline=False)
                
                total_uses_desc = str(max_uses) if max_uses else "Unlimited"
                embed.add_field(name="Total Available Uses", value=total_uses_desc, inline=False)


                embed.add_field(name="Applies To", value="All products (by default)", inline=False)
                embed.set_footer(text=f"To restrict this, use /discount-config code:{code}")


                await interaction.followup.send(embed=embed)
                print(f"LOG: Discount creation confirmation sent for '{code}'.")
            except ValueError:
                print("ERROR: Invalid input for discount creation (ValueError).")
                await interaction.followup.send("❌ Invalid input. Please check that percentage, date, and total uses are in the correct format.")
            except Exception as e:
                print(f"ERROR: Error creating discount: {e}")
                await interaction.followup.send(f"❌ An error occurred while creating the discount: `{e}`")

            
    async def handle_remove_discount_cmd(self, interaction: discord.Interaction):
        print(f"LOG: '{interaction.user.name}' opening RemoveDiscountModal.")
        await interaction.response.send_modal(RemoveDiscountModal(self))

    async def handle_remove_discount_modal_submit(self, interaction: discord.Interaction, modal: RemoveDiscountModal):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' submitting RemoveDiscountModal.")
        try:
            code = modal.code.value.upper()
            self.cursor_discounts.execute("SELECT * FROM discounts WHERE code = ?", (code,))
            if not self.cursor_discounts.fetchone():
                print(f"ERROR: Discount code '{code}' not found for removal.")
                return await interaction.followup.send(f"❌ Discount code `{code}` not found.")
            self.cursor_discounts.execute("UPDATE discounts SET is_active = 0 WHERE code = ?", (code,))
            self.conn_discounts.commit()
            print(f"LOG: Discount code '{code}' marked as inactive in '{DISCOUNTS_DB_NAME}'.")
            await interaction.followup.send(f"✅ Discount code `{code}` has been removed.")
            print(f"LOG: Discount removal confirmation sent for '{code}'.")
        except Exception as e:
            print(f"ERROR: Error removing discount: {e}")
            await interaction.followup.send(f"❌ An error occurred while removing the discount: `{e}`")

    async def handle_list_discounts(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' requested discount list.")
        try:
            self.cursor_discounts.execute("SELECT * FROM discounts WHERE is_active = 1 AND expires_at > ?", (datetime.datetime.now().isoformat(),))
            active_discounts = self.cursor_discounts.fetchall()
            if not active_discounts:
                print("LOG: No active discount codes found.")
                return await interaction.followup.send("ℹ️ No active discount codes available.")
            embed = discord.Embed(title="🎟️ Active Discount Codes", color=0x5865F2)
            for discount in active_discounts:
                uses_left = f"{discount['max_uses'] - discount['used_count']}/{discount['max_uses']} uses left" if discount['max_uses'] else "Unlimited total uses"
                
                usage_type_str = "One time per user"
                if discount['usage_type'] == 'multiple':
                    limit_str = f" (Limit: {discount['max_uses_per_user'] or 'Unlimited'})"
                    usage_type_str = f"Multiple times per user{limit_str}"

                applies_to = json.loads(discount['applies_to']) if discount['applies_to'] and discount['applies_to'] != '[]' else []
                applies_to_text = f"Applies to: {', '.join(applies_to)}" if applies_to else "Applies to all services"
                embed.add_field(
                    name=f"`{discount['code']}` - {discount['percent']}% off",
                    value=(
                        f"⏳ Expires: {datetime.datetime.fromisoformat(discount['expires_at']).strftime('%Y-%m-%d')}\n"
                        f"🔄 {usage_type_str}\n"
                        f"🌐 {uses_left}\n"
                        f"{applies_to_text}"
                    ),
                    inline=True
                )
            await interaction.followup.send(embed=embed)
            print("LOG: Discount list sent.")
        except Exception as e:
            print(f"ERROR: Error in discount list command: {e}")
            await interaction.followup.send(f"❌ An error occurred while listing discounts: `{e}`")
    
    async def handle_discount_usage(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' requested discount usage report.")
        try:
            self.cursor_discounts.execute("SELECT * FROM discount_usage")
            usage_data = self.cursor_discounts.fetchall()
            if not usage_data:
                return await interaction.followup.send("ℹ️ No discount codes have been used yet.", ephemeral=True)
            
            usage_list = [dict(row) for row in usage_data]
            
            with open("discount_usage.json", "w") as f:
                json.dump(usage_list, f, indent=4)
            
            await interaction.followup.send(file=discord.File("discount_usage.json"))
            os.remove("discount_usage.json")
            print("LOG: Discount usage report sent.")
            
        except Exception as e:
            print(f"ERROR: Error in discount usage command: {e}")
            await interaction.followup.send(f"❌ An error occurred while generating the discount usage report: `{e}`")

    async def autocomplete_discount_codes(self, interaction: discord.Interaction, current: str):
        
        self.cursor_discounts.execute("SELECT code FROM discounts WHERE is_active = 1 AND code LIKE ? LIMIT 25", (f'%{current}%',))
        codes = self.cursor_discounts.fetchall()
        return [app_commands.Choice(name=code['code'], value=code['code']) for code in codes]

    async def autocomplete_product_keys(self, interaction: discord.Interaction, current: str):
        

        self.cursor_products.execute("SELECT product_key FROM products WHERE is_active = 1 AND product_key LIKE ? LIMIT 25", (f'%{current}%',))
        keys = self.cursor_products.fetchall()
        return [app_commands.Choice(name=key['product_key'], value=key['product_key']) for key in keys]

    @app_commands.command(name="discount-config", description="Configure which products a discount code applies to.")
    @app_commands.checks.has_permissions(administrator=True)
    @app_commands.describe(
        code="The discount code to configure.",
        products="Comma-separated product keys (e.g., key1,key2). Leave empty to apply to all."
    )
    @app_commands.autocomplete(code=autocomplete_discount_codes, products=autocomplete_product_keys)
    async def discount_config(self, interaction: discord.Interaction, code: str, products: str = ""):
        
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' running discount-config for code '{code}'.")
        
        normalized_code = code.upper()
        self.cursor_discounts.execute("SELECT code FROM discounts WHERE code = ?", (normalized_code,))
        if not self.cursor_discounts.fetchone():
            return await interaction.followup.send(f"❌ Discount code `{normalized_code}` not found.")


        if not products.strip():
            self.cursor_discounts.execute("UPDATE discounts SET applies_to = ? WHERE code = ?", (None, normalized_code))
            self.conn_discounts.commit()
            print(f"LOG: Discount '{normalized_code}' restriction cleared. Applies to all products.")
            return await interaction.followup.send(f"✅ Discount `{normalized_code}` has been updated to apply to **all products**.")


        product_keys = [key.strip() for key in products.split(',') if key.strip()]
        
        self.cursor_products.execute("SELECT product_key FROM products WHERE is_active = 1")
        all_valid_keys = {row['product_key'] for row in self.cursor_products.fetchall()}
        
        invalid_keys = [key for key in product_keys if key not in all_valid_keys]
        if invalid_keys:
            valid_keys_str = ", ".join(all_valid_keys)
            return await interaction.followup.send(f"❌ The following product keys are invalid: `{', '.join(invalid_keys)}`.\nAvailable keys: `{valid_keys_str}`")


        json_products = json.dumps(product_keys)
        self.cursor_discounts.execute("UPDATE discounts SET applies_to = ? WHERE code = ?", (json_products, normalized_code))
        self.conn_discounts.commit()
        
        print(f"LOG: Discount '{normalized_code}' configured for products: {product_keys}")
        await interaction.followup.send(f"✅ Discount `{normalized_code}` is now restricted to products: `{', '.join(product_keys)}`.")


    @app_commands.command(name="apply-tag", description="Apply a tag to an order and trigger associated actions.")
    async def apply_tag(self, interaction: discord.Interaction, order_id: str, tag_name: str, note_message: str = None):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: [apply-tag] Command initiated by {interaction.user.name} for order {order_id} with tag {tag_name}.")
        self.cursor_setup.execute("SELECT staff_role_id FROM setup WHERE guild_id = ?", (str(interaction.guild_id),))
        setup_data = self.cursor_setup.fetchone()
        if not interaction.user.guild_permissions.administrator:
            if not setup_data or not interaction.user.get_role(int(setup_data["staff_role_id"])):
                print(f"ERROR: [apply-tag] Permission check failed for user {interaction.user.name}.")
                return await interaction.followup.send("❌ You do not have permission to use this command.", ephemeral=True)
        print(f"LOG: [apply-tag] Permission check passed for user {interaction.user.name}.")
        response_message = ""
        try:
            print(f"LOG: [apply-tag] Looking for order {order_id.upper()} in '{ORDER_TICKETS_DB_NAME}'.")
            self.cursor_order_tickets.execute("SELECT * FROM orders WHERE order_number = ?", (order_id.upper(),))
            order_data = self.cursor_order_tickets.fetchone()
            if not order_data:
                response_message = f"❌ Order with ID `{order_id}` not found."
                print(f"ERROR: [apply-tag] Order with ID '{order_id}' not found for tagging.")
                await interaction.followup.send(response_message, ephemeral=True)
                return
            print(f"LOG: [apply-tag] Order data found for order {order_id}.")
            self.cursor_order_tickets.execute("UPDATE orders SET tag = ? WHERE order_number = ?", (tag_name.lower(), order_id.upper()))
            self.conn_order_tickets.commit()
            print(f"LOG: [apply-tag] Order '{order_id}' tagged as '{tag_name}' in '{ORDER_TICKETS_DB_NAME}'.")
            response_message += f"✅ Order `{order_id}` tagged as `{tag_name}`."
            self.cursor_tags.execute("SELECT channel_id FROM order_tags_channels WHERE tag_name = ?", (tag_name.lower(),))
            tag_channel_config = self.cursor_tags.fetchone()
            if tag_channel_config:
                target_channel = self.bot.get_channel(int(tag_channel_config["channel_id"]))
                if target_channel:
                    print(f"LOG: [apply-tag] Target channel '{target_channel.name}' found for tag '{tag_name}'.")
                    items_list = json.loads(order_data['items'])
                    items_value = "\n".join([f"• {item['name']} (€{item['price']:.2f})" for item in items_list]) if items_list else "No items"
                    tag_embed = discord.Embed(
                        title=f"🏷️ Order #{order_id} Tagged: `{tag_name}`",
                        color=discord.Color.blue()
                    )
                    tag_embed.add_field(name="Customer", value=f"<@{order_data['user_id']}>", inline=True)
                    tag_embed.add_field(name="Created Date", value=datetime.datetime.fromisoformat(order_data['created_at']).strftime("%Y-%m-%d %H:%M:%S"), inline=True)
                    tag_embed.add_field(name="Price (Original)", value=f"€{order_data['subtotal']:.2f}", inline=True)
                    if order_data['discount_code']:
                        tag_embed.add_field(name="Discount Applied", value=f"{order_data['discount_code']} ({order_data['discount_amount']}%)", inline=True)
                    tag_embed.add_field(name="Price (Final)", value=f"€{order_data['total_amount']:.2f}", inline=True)
                    tag_embed.add_field(name="Items", value=items_value, inline=False)
                    if note_message:
                        tag_embed.add_field(name="Note", value=note_message, inline=False)
                    tag_embed.set_footer(text=f"Tagged by {interaction.user.name}", icon_url=interaction.user.display_avatar.url)
                    tag_embed.timestamp = datetime.datetime.now()
                    await target_channel.send(embed=tag_embed)
                    print(f"LOG: [apply-tag] Informational message sent to channel {target_channel.name} for tag '{tag_name}'.")
                else:
                    print(f"WARNING: [apply-tag] Configured channel for tag '{tag_name}' not found. Message not sent.")
                    response_message += f"\n⚠️ Configured channel for tag `{tag_name}` not found. Message not sent."
            else:
                print(f"LOG: [apply-tag] No specific channel configured for tag '{tag_name}'. No informational message posted.")
                response_message += f"\nℹ️ No specific channel configured for tag `{tag_name}`. No informational message posted."
            self.cursor_tags.execute("SELECT functions, status_change FROM order_tag_functions WHERE tag_name = ?", (tag_name.lower(),))
            functions_config = self.cursor_tags.fetchone()
            if functions_config:
                if functions_config["status_change"]:
                    new_status = functions_config["status_change"]
                    order_user = await self.bot.fetch_user(order_data['user_id'])
                    await self.update_order_status(order_data['order_number'], new_status, order_user, note_message)
                    response_message += f"\n✅ Order status automatically updated to `{new_status}`."
                if functions_config["functions"]:
                    function_names = json.loads(functions_config["functions"])
                    print(f"LOG: [apply-tag] Functions configured for tag '{tag_name}': {function_names}")
                    for function_name in function_names:
                        if hasattr(self, function_name) and callable(getattr(self, function_name)):
                            print(f"LOG: [apply-tag] Attempting to execute function '{function_name}'.")
                            await getattr(self, function_name)(dict(order_data), interaction)
                            response_message += f"\n✅ Associated function `{function_name}` executed."
                            print(f"LOG: [apply-tag] Associated function '{function_name}' executed for tag '{tag_name}'.")
                        else:
                            response_message += f"\n⚠️ Function `{function_name}` configured for tag `{tag_name}` not found or is not callable."
                            print(f"ERROR: [apply-tag] Function '{function_name}' configured for tag '{tag_name}' not found or is not callable.")
        except Exception as e:
            response_message = f"❌ An error occurred while tagging the order: `{e}`"
            print(f"ERROR: [apply-tag] Unhandled exception during apply-tag command: {e}")
        finally:
            try:
                print(f"LOG: [apply-tag] Attempting to send final followup message: '{response_message}'.")
                await interaction.followup.send(response_message, ephemeral=True)
                print(f"LOG: [apply-tag] Final followup message sent successfully.")
            except Exception as followup_e:
                print(f"ERROR: [apply-tag] Failed to send final followup message: {followup_e}")

    @app_commands.command(name="set-tag-channel", description="Sets the channel for a specific order tag's informational messages.")
    @app_commands.checks.has_permissions(administrator=True)
    @app_commands.describe(
        tag_name="The name of the tag (e.g., 'complete', 'shipped').",
        channel="The channel where messages for this tag should be sent."
    )
    async def set_tag_channel(self, interaction: discord.Interaction, tag_name: str, channel: discord.TextChannel):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' setting channel for tag '{tag_name}' to {channel.name}.")
        try:
            self.cursor_tags.execute("INSERT OR REPLACE INTO order_tags_channels (tag_name, channel_id) VALUES (?, ?)",
                (tag_name.lower(), str(channel.id)))
            self.conn_tags.commit()
            print(f"LOG: Channel for tag '{tag_name}' saved in '{TAGS_DB_NAME}'.")
            await interaction.followup.send(f"✅ Messages for tag `{tag_name}` will now be sent to {channel.mention}.")
        except Exception as e:
            print(f"ERROR: Error in set-tag-channel command: {e}")
            await interaction.followup.send(f"❌ An error occurred while setting the channel for the tag: `{e}`")

    async def autocomplete_functions(self, interaction: discord.Interaction, current: str):
        functions = [
            'close_ticket_by_order_id', 
            'mark_order_complete', 
            'mark_order_as_failed',
            'mark_order_as_shipped', 
            'send_order_details_to_channel'
        ]
        return [
            app_commands.Choice(name=func, value=func)
            for func in functions if current.lower() in func.lower()
        ]

    async def autocomplete_statuses(self, interaction: discord.Interaction, current: str):
        self.cursor_statuses.execute("SELECT name FROM statuses")
        statuses = self.cursor_statuses.fetchall()
        return [
            app_commands.Choice(name=status['name'], value=status['name'])
            for status in statuses if current.lower() in status['name'].lower()
        ]

    @app_commands.command(name="create-tag", description="Creates a custom tag and links multiple bot functions to it.")
    @app_commands.checks.has_permissions(administrator=True)
    @app_commands.describe(
        tag_name="The name of the tag (e.g., 'complete', 'refunded').",
        function_name1="The first function to execute.",
        function_name2="The second function to execute (optional).",
        function_name3="The third function to execute (optional).",
        function_name4="The fourth function to execute (optional).",
        function_name5="The fifth function to execute (optional).",
        order_status_to_set="Set a new order status when this tag is applied."
    )
    @app_commands.autocomplete(function_name1=autocomplete_functions)
    @app_commands.autocomplete(function_name2=autocomplete_functions)
    @app_commands.autocomplete(function_name3=autocomplete_functions)
    @app_commands.autocomplete(function_name4=autocomplete_functions)
    @app_commands.autocomplete(function_name5=autocomplete_functions)
    @app_commands.autocomplete(order_status_to_set=autocomplete_statuses)
    async def create_tag(self, interaction: discord.Interaction, tag_name: str, order_status_to_set: str = None, 
                              function_name1: str = None, function_name2: str = None, function_name3: str = None, 
                              function_name4: str = None, function_name5: str = None):
        await interaction.response.defer(ephemeral=True)
        
        all_function_names = [f for f in [function_name1, function_name2, function_name3, function_name4, function_name5] if f is not None]

        print(f"LOG: '{interaction.user.name}' creating tag '{tag_name}' linked to functions: {all_function_names} and status: {order_status_to_set}.")

        try:
            valid_functions = []
            for func_name in all_function_names:
                if not hasattr(self, func_name) or not callable(getattr(self, func_name)):
                    print(f"ERROR: Function '{func_name}' does not exist or is not callable.")
                    return await interaction.followup.send(f"❌ Function `{func_name}` does not exist or is not callable within the bot's code. Please ensure it's a valid method name in the OrderSystem cog.")
                valid_functions.append(func_name)
            if order_status_to_set:
                self.cursor_statuses.execute("SELECT name FROM statuses WHERE name = ?", (order_status_to_set.lower(),))
                if not self.cursor_statuses.fetchone():
                    return await interaction.followup.send(f"❌ The status `{order_status_to_set}` is not a valid status. Please use `/add-status` to create it first.")
            self.cursor_tags.execute("INSERT OR REPLACE INTO order_tag_functions (tag_name, functions, status_change) VALUES (?, ?, ?)",
                (tag_name.lower(), json.dumps(valid_functions) if valid_functions else None, order_status_to_set))
            self.conn_tags.commit()
            status_text = f" and will update the status to `{order_status_to_set}`." if order_status_to_set else "."
            functions_text = f" and linked to functions: `{', '.join(valid_functions)}`" if valid_functions else ""
            print(f"LOG: Tag '{tag_name}' created in '{TAGS_DB_NAME}' with status '{order_status_to_set}' and functions '{valid_functions}'.")
            await interaction.followup.send(f"✅ Tag `{tag_name}` created{functions_text}{status_text}")
        except Exception as e:
            print(f"ERROR: Error in create-tag command: {e}")
            await interaction.followup.send(f"❌ An error occurred while creating the tag and linking the functions: `{e}`")

    async def update_order_status(self, order_number: str, new_status: str, user, note_message: str = None):
        print(f"LOG: [update_order_status] Executing for order {order_number} to status {new_status}.")
        self.cursor_order_tickets.execute("SELECT * FROM orders WHERE order_number = ?", (order_number,))
        order_data = self.cursor_order_tickets.fetchone()
        if not order_data:
            print(f"ERROR: Order #{order_number} not found for status update.")
            return
        self.cursor_order_tickets.execute("UPDATE orders SET status = ? WHERE order_number = ?", (new_status, order_number))
        self.cursor_order_tickets.execute("UPDATE tracking SET status = ? WHERE order_number = ?", (new_status, order_number))
        self.conn_order_tickets.commit()
        print(f"LOG: Order {order_number} status updated to {new_status} in '{ORDER_TICKETS_DB_NAME}'.")
        
        await self.update_all_status_embeds(self.bot, order_number, new_status, user, note_message)
        print(f"LOG: [update_order_status] Status embeds updated for order {order_number}.")
        
    async def mark_order_complete(self, order_data, interaction):
        print(f"LOG: [mark_order_complete] Executing for order {order_data['order_number']}.")
        try:
            pass
        except Exception as e:
            print(f"ERROR: [mark_order_complete] Error marking order {order_data['order_number']} complete: {e}")

    async def mark_order_as_failed(self, order_data, interaction):
        print(f"LOG: [mark_order_as_failed] Executing for order {order_data['order_number']}.")
        try:
            pass
        except Exception as e:
            print(f"ERROR: [mark_order_as_failed] Error marking order {order_data['order_number']} failed: {e}")

    async def mark_order_as_shipped(self, order_data, interaction):
        print(f"LOG: [mark_order_as_shipped] Executing for order {order_data['order_number']}.")
        try:
            pass
        except Exception as e:
            print(f"ERROR: [mark_order_as_shipped] Error marking order {order_data['order_number']} shipped: {e}")

    async def send_order_details_to_channel(self, order_data, interaction):
        print(f"LOG: [send_order_details_to_channel] Executing for order {order_data['order_number']}.")
        try:
            self.cursor_tags.execute("SELECT channel_id FROM order_tags_channels WHERE tag_name = ?", (order_data['tag'],))
            tag_channel_config = self.cursor_tags.fetchone()
            if tag_channel_config:
                target_channel = self.bot.get_channel(int(tag_channel_config['channel_id']))
                if target_channel:
                    items_list = json.loads(order_data['items'])
                    items_value = "\n".join([f"• {item['name']} (€{item['price']:.2f})" for item in items_list]) if items_list else "No items"
                    details_embed = discord.Embed(
                        title=f"📦 Order Details for #{order_data['order_number']}",
                        description=f"This order was tagged as **`{order_data['tag']}`**.",
                        color=discord.Color.blue()
                    )
                    details_embed.add_field(name="Customer", value=f"<@{order_data['user_id']}>", inline=True)
                    details_embed.add_field(name="Created Date", value=datetime.datetime.fromisoformat(order_data['created_at']).strftime("%Y-%m-%d %H:%M:%S"), inline=True)
                    details_embed.add_field(name="Price", value=f"€{order_data['total_amount']:.2f}", inline=True)
                    details_embed.add_field(name="Items", value=items_value, inline=False)
                    await target_channel.send(embed=details_embed)
                    print(f"LOG: [send_order_details_to_channel] Order details sent to channel {target_channel.id}.")
                else:
                    print(f"WARNING: [send_order_details_to_channel] Configured channel for tag '{order_data['tag']}' not found. Message not sent.")
            else:
                print(f"WARNING: [send_order_details_to_channel] No channel configured for tag '{order_data['tag']}'.")
        except Exception as e:
            print(f"ERROR: [send_order_details_to_channel] Error sending order details: {e}")
            
    async def close_ticket_by_order_id(self, order_data, interaction):
        print(f"LOG: [close_ticket_by_order_id] Executing for order {order_data['order_number']}.")
        try:
            self.cursor_order_tickets.execute("SELECT * FROM tickets WHERE order_number = ? AND guild_id = ?", (order_data["order_number"], str(interaction.guild_id)))
            ticket_data = self.cursor_order_tickets.fetchone()
            
            if ticket_data:
                print(f"LOG: [close_ticket_by_order_id] Ticket data found for order {order_data['order_number']}.")
                ticket_channel = self.bot.get_channel(int(ticket_data["channel_id"]))
                if ticket_channel:
                    self.cursor_setup.execute("SELECT * FROM setup WHERE guild_id = ?", (str(interaction.guild_id),))
                    setup_data = self.cursor_setup.fetchone()
                    
                    if setup_data and setup_data["transcript_channel_id"]:
                        transcript_channel = self.bot.get_channel(int(setup_data["transcript_channel_id"]))
                        if transcript_channel:
                            transcript_messages = [m async for m in ticket_channel.history(limit=None, oldest_first=True)]
                            transcript_content = "\n".join([f"[{m.created_at.strftime('%Y-%m-%d %H:%M:%S')}] {m.author.name}: {m.content}" for m in transcript_messages])
                            transcript_file = discord.File(
                                io.StringIO(transcript_content),
                                filename=f"transcript-{ticket_channel.name}.txt"
                            )
                            transcript_embed = discord.Embed(
                                title="📒 Ticket Transcript",
                                description=f"Ticket for <@{ticket_data['user_id']}> (`{ticket_data['user_id']}`)",
                                color=discord.Color.blue()
                            )
                            await transcript_channel.send(embed=transcript_embed, file=transcript_file)
                            print(f"LOG: Transcript sent to channel {transcript_channel.name}.")
                            
                    self.cursor_order_tickets.execute("DELETE FROM tickets WHERE channel_id = ?", (str(ticket_channel.id),))
                    self.conn_order_tickets.commit()
                    print(f"LOG: Ticket deleted from '{ORDER_TICKETS_DB_NAME}' for channel {ticket_channel.id}.")
                    
                    if ticket_data["ticket_type"] == "purchase" and setup_data["reviews_channel_id"]:
                        reviews_channel = self.bot.get_channel(int(setup_data["reviews_channel_id"]))
                        if reviews_channel:
                            try:
                                review_embed = discord.Embed(
                                    title="⭐ Rate Your Experience!",
                                    description="How was your experience with our service? Please leave a rating and feedback.",
                                    color=discord.Color.gold()
                                )
                                review_view = RatingView(order_data["order_number"])
                                ticket_user = await self.bot.fetch_user(ticket_data["user_id"])
                                await ticket_user.send(embed=review_embed, view=review_view)
                                print(f"LOG: Review DM sent to user {ticket_user.id} for order {order_data['order_number']}.")
                            except Exception as dm_e:
                                print(f"ERROR: Failed to send review DM to user {ticket_user.id}: {dm_e}")
                    
                    await ticket_channel.delete(reason=f"Ticket closed by order tag action for order {order_data['order_number']}")
                    print(f"LOG: Ticket channel {ticket_channel.id} deleted.")
                else:
                    print(f"WARNING: [close_ticket_by_order_id] Ticket channel for order {order_data['order_number']} not found. Removing from DB.")
                    self.cursor_order_tickets.execute("DELETE FROM tickets WHERE order_number = ? AND guild_id = ?", (order_data["order_number"], str(interaction.guild_id)))
                    self.conn_order_tickets.commit()
            else:
                print(f"LOG: [close_ticket_by_order_id] No active ticket found for order {order_data['order_number']} to close.")
        except Exception as e:
            print(f"ERROR: [close_ticket_by_order_id] Error closing ticket for order {order_data['order_number']}: {e}")

    async def show_purchase_products(self, interaction):
        print(f"LOG: '{interaction.user.name}' requested to show purchase products.")
        try:
            self.cursor_products.execute("SELECT * FROM products WHERE is_active = 1 ORDER BY price ASC")
            products = self.cursor_products.fetchall()
            if not products:
                print("LOG: No products available for purchase.")
                return await interaction.followup.send("❌ No products available for purchase at the moment.", ephemeral=True)
            embed = discord.Embed(
                title="🛒 Select a Product to Purchase",
                description="Choose the service you would like to order. A purchase ticket will be created for you with all the details.",
                color=0x5865F2
            )
            for product in products:
                emoji_to_use = "🛒"
                if product['emoji'] and validate_emoji(product['emoji']):
                    emoji_to_use = product['emoji']

                embed.add_field(
                    name=f"{emoji_to_use} {product['name']}",
                    value=f"**€{product['price']:.2f}**\n{product['description'] or 'No description'}",
                    inline=True
                )
            view = ProductSelectView(products, self.bot)
            await interaction.followup.send(embed=embed, view=view, ephemeral=True)
            print("LOG: Purchase products displayed.")
        except Exception as e:
            print(f"ERROR: Error in show_purchase_products: {e}")
            await interaction.followup.send(f"❌ An error occurred while loading products: `{e}`", ephemeral=True)

    async def create_purchase_ticket(self, interaction, product_key):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' initiating purchase ticket for product: {product_key}.")
        try:
            self.cursor_order_tickets.execute("SELECT * FROM tickets WHERE user_id = ? AND guild_id = ?", (str(interaction.user.id), str(interaction.guild_id)))
            existing_ticket = self.cursor_order_tickets.fetchone()
            if existing_ticket:
                channel = self.bot.get_channel(int(existing_ticket["channel_id"]))
                if channel:
                    embed = discord.Embed(
                        title="Ticket Already Exists", 
                        description=f"You already have an active ticket in this server: {channel.mention}", 
                        color=discord.Color.orange()
                    )
                    print(f"LOG: Existing ticket found for user {interaction.user.id} in guild {interaction.guild_id}.")
                    return await interaction.followup.send(embed=embed, ephemeral=True)
                else:
                    self.cursor_order_tickets.execute("DELETE FROM tickets WHERE user_id = ? AND guild_id = ?", (str(interaction.user.id), str(interaction.guild_id)))
                    self.conn_order_tickets.commit()
                    print(f"LOG: Stale ticket record deleted for user {interaction.user.id}.")
                    await interaction.followup.send("Detected a stale ticket record. Please try creating your ticket again.", ephemeral=True)
                    return
            self.cursor_products.execute("SELECT * FROM products WHERE product_key = ? AND is_active = 1", (product_key,))
            product = self.cursor_products.fetchone()
            if not product:
                print(f"ERROR: Product '{product_key}' not found or inactive for purchase ticket creation.")
                return await interaction.followup.send(f"❌ Product not found or inactive: `{product_key}`", ephemeral=True)
            self.cursor_setup.execute("SELECT * FROM setup WHERE guild_id = ?", (str(interaction.guild.id),))
            guild_config = self.cursor_setup.fetchone()
            if not guild_config:
                print(f"ERROR: Ticket system not configured for guild {interaction.guild.id}.")
                return await interaction.followup.send("❌ Ticket system is not configured correctly.", ephemeral=True)
            overwrites = {
                interaction.guild.default_role: discord.PermissionOverwrite(view_channel=False),
                interaction.user: discord.PermissionOverwrite(view_channel=True, send_messages=True),
                interaction.guild.get_role(int(guild_config["staff_role_id"])): discord.PermissionOverwrite(view_channel=True, send_messages=True)
            }
            if guild_config["supporter_role_ids"]:
                supporter_roles = json.loads(guild_config["supporter_role_ids"])
                for role_id in supporter_roles:
                    role = interaction.guild.get_role(int(role_id))
                    if role:
                        overwrites[role] = discord.PermissionOverwrite(view_channel=True, send_messages=True)
            order_number = generate_short_id()
            new_channel = await interaction.guild.create_text_channel(
                name=f"purchase-{product['name'].lower().replace(' ', '-')}-{order_number}",
                category=self.bot.get_channel(int(guild_config["purchase_category_id"])),
                overwrites=overwrites
            )
            print(f"LOG: Created new channel {new_channel.name} for purchase ticket.")
            items_list = [{"name": product["name"], "price": product["price"], "product_key": product_key}]
            items_json = json.dumps(items_list)
            
            self.cursor_order_tickets.execute("""
                INSERT INTO orders (user_id, guild_id, order_number, items, status, subtotal, total_amount, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                str(interaction.user.id),
                str(interaction.guild_id),
                order_number, 
                items_json, 
                "processing",
                product["price"],
                product["price"],
                datetime.datetime.now().isoformat(), 
                datetime.datetime.now().isoformat()
            ))
            order_id = self.cursor_order_tickets.lastrowid
            self.conn_order_tickets.commit()
            
            self.cursor_order_tickets.execute("SELECT * FROM orders WHERE order_id = ?", (order_id,))
            order_data = self.cursor_order_tickets.fetchone()
            if not order_data:
                raise Exception("Failed to retrieve new order data.")

            print(f"LOG: Order created in '{ORDER_TICKETS_DB_NAME}': Order Number={order_number}, User ID={interaction.user.id}, Guild ID={interaction.guild_id}, Items={items_json}, Subtotal={product['price']}.")
            await interaction.followup.send(f"✅ Your purchase ticket has been created: {new_channel.mention}", ephemeral=True)
            
            emoji_to_use = "❓"
            if product['emoji'] and validate_emoji(product['emoji']):
                emoji_to_use = product['emoji']

            product_embed = discord.Embed(
                title=product["embed_title"] or f"{emoji_to_use} {product['name']}",
                description=product["embed_description"] or f"Thank you for your interest in **{product['name']}**!\n\nOur team will process your order shortly.",
                color=product["embed_color"] or 0x5865F2
            )
            product_embed.add_field(name="💰 Price", value=f"€{product['price']:.2f}", inline=True)
            product_embed.add_field(name="👤 Customer", value=interaction.user.mention, inline=True)
            product_embed.add_field(name="📅 Created", value=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), inline=True)
            product_embed.add_field(name="📦 Order ID", value=order_number, inline=True)
            product_embed.add_field(name="Current Status", value=format_status("processing"), inline=True)
            product_embed.set_thumbnail(url=NEW_IMAGE_URL)
            product_embed.set_footer(text="Our team will contact you shortly!", icon_url=NEW_IMAGE_URL)
            view = TicketView.from_cog(self, "purchase", product_key)
            sent_message = await new_channel.send(f"Hello {interaction.user.mention}! 👋", embed=product_embed, view=view)
            self.cursor_order_tickets.execute("INSERT INTO tickets (username, user_id, guild_id, tickets_count, channel_id, ticket_message_id, ticket_type, product_key, order_number) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (interaction.user.name, str(interaction.user.id), str(interaction.guild_id), 1, str(new_channel.id), str(sent_message.id), "purchase", product_key, order_number))
            self.conn_order_tickets.commit()
            print(f"LOG: Ticket created in '{ORDER_TICKETS_DB_NAME}': Channel ID={new_channel.id}, Message ID={sent_message.id}, Order Number={order_number}.")
            
            status_embed = await create_status_embed(order_data, "processing")
            status_message = await new_channel.send(embed=status_embed)
            
            self.cursor_order_tickets.execute("""
                INSERT INTO tracking (order_id, order_number, channel_id, status_message_id, ticket_message_id, history, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                order_data["order_id"],
                order_data["order_number"],
                str(new_channel.id),
                str(status_message.id),
                str(sent_message.id),
                json.dumps([{"status": "processing", "changed_at": datetime.datetime.now().isoformat(), "changed_by": str(self.bot.user.id)}]),
                datetime.datetime.now().isoformat(),
                datetime.datetime.now().isoformat()
            ))
            self.conn_order_tickets.commit()
            
            print(f"LOG: Status embed sent and tracking updated for order {order_number}.")
            if product["has_instructions"] and product["instruction_embed_title"] and product["instruction_embed_description"]:
                instruction_embed = discord.Embed(
                    title=product["instruction_embed_title"],
                    description=product["instruction_embed_description"],
                    color=product["instruction_embed_color"] or 0x57F287
                )
                instruction_embed.set_footer(text="Please provide the requested information so we can get started!", icon_url=NEW_IMAGE_URL)
                await new_channel.send(embed=instruction_embed)
                print(f"LOG: Instruction embed sent to channel {new_channel.id}.")
        except Exception as e:
            print(f"ERROR: Error in create_purchase_ticket: {e}")
            await interaction.followup.send(f"❌ An error occurred while creating the purchase ticket: `{e}`", ephemeral=True)

    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):
        if interaction.type == discord.InteractionType.component:
            custom_id = interaction.data["custom_id"]
            print(f"LOG: Component interaction detected: {custom_id} by {interaction.user.name}.")
            if custom_id == "ticketsystemid":
                await self.handle_ticket_select(interaction)
            elif custom_id == "product_select":
                await self.handle_product_select(interaction)
            elif custom_id.startswith("rate_"):
                parts = custom_id.split("_")
                stars = int(parts[1])
                order_number = parts[2]
                await self.handle_rate_service_stars(interaction, stars, order_number)
            elif custom_id == "close":
                await self.handle_close_ticket(interaction)
            elif custom_id == "claim":
                await self.handle_claim_ticket(interaction)
            elif custom_id == "transcript":
                await self.handle_transcript_ticket(interaction)
            elif custom_id == "show_supporters":
                await self.handle_show_supporters(interaction)
            elif custom_id == "apply_discount":
                await self.handle_apply_discount_modal(interaction)
            elif custom_id == "startOrder":
                await self.handle_start_order(interaction)
            elif custom_id == "products_dropdown":
                await self.handle_products_dropdown_select(interaction)
            elif custom_id == "selectService":
                await self.handle_select_service(interaction)
            elif custom_id == "selectPayment":
                await self.handle_select_payment(interaction)
            elif custom_id == "add_more":
                await self.handle_add_more_services(interaction)
            elif custom_id == "remove_discount":
                await self.handle_remove_discount(interaction)
            elif custom_id == "final_confirm":
                await self.handle_final_confirm(interaction)
            elif custom_id == "cancel_order":
                await self.handle_cancel_order(interaction)
            elif custom_id == "generate_invoice":
                await self.handle_generate_invoice(interaction)
            elif custom_id == "check_status":
                await self.handle_check_status(interaction)
            elif custom_id == "yes_close":
                await self.handle_close_confirm(interaction, True)
            elif custom_id == "no_close":
                await self.handle_close_confirm(interaction, False)
        elif interaction.type == discord.InteractionType.modal_submit:
            custom_id = interaction.data["custom_id"]
            print(f"LOG: Modal submit interaction detected: {custom_id} by {interaction.user.name}.")
            if custom_id.startswith("otherTicketModal_"):
                await self.handle_other_ticket_modal_submit(interaction, custom_id)
            elif custom_id == "discountModal":
                await self.handle_apply_discount_modal_submit(interaction, interaction.data['components'][0]['components'][0]['value'])
            elif custom_id.startswith("feedback_modal_"):
                parts = custom_id.split('_')
                order_number = parts[2]
                stars = int(parts[3])
                await self.handle_feedback_modal_submit(interaction, stars, order_number)
            elif custom_id == "create_discount_modal":
                pass
            elif custom_id == "remove_discount_modal":
                pass

    async def handle_ticket_select(self, interaction):
        value = interaction.data["values"][0]
        print(f"LOG: Ticket select menu interaction: {value} by {interaction.user.name}.")
        conn_order_tickets = sqlite3.connect(ORDER_TICKETS_DB_NAME)
        conn_order_tickets.row_factory = sqlite3.Row
        cursor_order_tickets = conn_order_tickets.cursor()
        cursor_order_tickets.execute("SELECT * FROM tickets WHERE user_id = ? AND guild_id = ?", (str(interaction.user.id), str(interaction.guild_id)))
        existing_ticket = cursor_order_tickets.fetchone()
        conn_order_tickets.close()
        if existing_ticket:
            channel = self.bot.get_channel(int(existing_ticket["channel_id"]))
            if channel:
                embed = discord.Embed(title="Ticket Already Open", description=f"You already have an active ticket in this server: {channel.mention}", color=discord.Color.red())
                print(f"LOG: Existing ticket found for user {interaction.user.id} in guild {interaction.guild_id}.")
                return await interaction.response.send_message(embed=embed, ephemeral=True)
            else:
                conn_order_tickets = sqlite3.connect(ORDER_TICKETS_DB_NAME)
                cursor_order_tickets = conn_order_tickets.cursor()
                cursor_order_tickets.execute("DELETE FROM tickets WHERE user_id = ? AND guild_id = ?", (str(interaction.user.id), str(interaction.guild_id)))
                conn_order_tickets.commit()
                conn_order_tickets.close()
                print(f"LOG: Stale ticket record deleted for user {interaction.user.id}.")
                await interaction.followup.send("Detected a stale ticket record. Please try creating your ticket again.", ephemeral=True)
        if value == "purchase":
            await interaction.response.defer(ephemeral=True)
            await self.show_purchase_products(interaction)
            return
        await interaction.response.defer(ephemeral=True)
        if value == "other":
            await self.handle_other_ticket_modal(interaction)
        else:
            await self.create_ticket(interaction, value)

    async def handle_product_select(self, interaction):
        selected_product_key = interaction.data["values"][0]
        print(f"LOG: Product selected: {selected_product_key} by {interaction.user.name}.")
        await self.create_purchase_ticket(interaction, selected_product_key)

    async def handle_other_ticket_modal(self, interaction):
        print(f"LOG: '{interaction.user.name}' opening other ticket modal.")
        modal = ui.Modal(title="Provide Ticket Reason")
        modal.custom_id = f"otherTicketModal_{interaction.user.id}"
        reason_input = ui.TextInput(
            label="Why do you want to create a ticket?",
            custom_id="reason",
            style=discord.TextStyle.short,
            required=True
        )
        modal.add_item(reason_input)
        await interaction.response.send_modal(modal)

    async def handle_other_ticket_modal_submit(self, interaction, custom_id):
        await interaction.response.defer(ephemeral=True)
        reason = interaction.data['components'][0]['components'][0]['value']
        print(f"LOG: '{interaction.user.name}' submitting other ticket modal with reason: {reason}.")
        await self.create_ticket(interaction, "other", reason)
    
    async def create_ticket(self, interaction, ticket_type, reason=None):
        conn_order_tickets = sqlite3.connect(ORDER_TICKETS_DB_NAME)
        conn_order_tickets.row_factory = sqlite3.Row
        cursor_order_tickets = conn_order_tickets.cursor()
        cursor_order_tickets.execute("SELECT * FROM tickets WHERE user_id = ? AND guild_id = ?", (str(interaction.user.id), str(interaction.guild_id)))
        existing_ticket = cursor_order_tickets.fetchone()
        conn_order_tickets.close()
        if existing_ticket:
            channel = self.bot.get_channel(int(existing_ticket["channel_id"]))
            if channel:
                embed = discord.Embed(title="Ticket Already Open", description=f"You already have an active ticket in this server: {channel.mention}", color=discord.Color.red())
                print(f"LOG: Existing ticket found for user {interaction.user.id} in guild {interaction.guild_id}.")
                return await interaction.followup.send(embed=embed, ephemeral=True)
            else:
                conn_order_tickets = sqlite3.connect(ORDER_TICKETS_DB_NAME)
                cursor_order_tickets = conn_order_tickets.cursor()
                cursor_order_tickets.execute("DELETE FROM tickets WHERE user_id = ? AND guild_id = ?", (str(interaction.user.id), str(interaction.guild_id)))
                conn_order_tickets.commit()
                conn_order_tickets.close()
                print(f"LOG: Stale ticket record deleted for user {interaction.user.id}.")
                await interaction.followup.send("Detected a stale ticket record. Please try creating your ticket again.", ephemeral=True)
        self.cursor_setup.execute("SELECT * FROM setup WHERE guild_id = ?", (str(interaction.guild.id),))
        guild_config = self.cursor_setup.fetchone()
        if not guild_config:
            print(f"ERROR: Ticket system not configured for guild {interaction.guild.id}.")
            return await interaction.followup.send("Ticket system is not configured correctly.", ephemeral=True)
        category_id = None
        if ticket_type == "support":
            category_id = guild_config["support_category_id"]
        elif ticket_type == "other":
            category_id = guild_config["other_category_id"]
        overwrites = {
            interaction.guild.default_role: discord.PermissionOverwrite(view_channel=False),
            interaction.user: discord.PermissionOverwrite(view_channel=True),
            interaction.guild.get_role(int(guild_config["staff_role_id"])): discord.PermissionOverwrite(view_channel=True)
        }
        if guild_config["supporter_role_ids"]:
            supporter_roles = json.loads(guild_config["supporter_role_ids"])
            for role_id in supporter_roles:
                role = interaction.guild.get_role(int(role_id))
                if role:
                    overwrites[role] = discord.PermissionOverwrite(view_channel=True)
        new_channel = await interaction.guild.create_text_channel(
            name=f"{ticket_type}-{interaction.user.name}",
            category=self.bot.get_channel(int(category_id)),
            overwrites=overwrites
        )
        print(f"LOG: Created new channel {new_channel.name} for {ticket_type} ticket.")
        await interaction.followup.send(f"Your {ticket_type} ticket has been created: {new_channel.mention}", ephemeral=True)
        ticket_embed = discord.Embed(
            title=f"{ticket_type.capitalize()} Ticket",
            description=f"Hello {interaction.user.mention}!\n\nOur team will contact you shortly.\n" + (f"**Reason:** {reason}" if reason else ""),
            color=discord.Color.green()
        )
        view = TicketView.from_cog(self, ticket_type)
        sent_message = await new_channel.send(embed=ticket_embed, view=view)
        conn_order_tickets = sqlite3.connect(ORDER_TICKETS_DB_NAME)
        conn_order_tickets.row_factory = sqlite3.Row
        cursor_order_tickets = conn_order_tickets.cursor()
        cursor_order_tickets.execute("INSERT INTO tickets (username, user_id, guild_id, tickets_count, channel_id, ticket_message_id, ticket_type) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (interaction.user.name, str(interaction.user.id), str(interaction.guild.id), 1, str(new_channel.id), str(sent_message.id), ticket_type))
        conn_order_tickets.commit()
        conn_order_tickets.close()
        print(f"LOG: Non-purchase ticket created in '{ORDER_TICKETS_DB_NAME}': Channel ID={new_channel.id}, Message ID={sent_message.id}, Ticket Type={ticket_type}.")
    
    async def handle_close_ticket(self, interaction):
        await interaction.response.defer()
        print(f"LOG: '{interaction.user.name}' attempting to close ticket in channel {interaction.channel.id}.")
        self.cursor_setup.execute("SELECT staff_role_id FROM setup WHERE guild_id = ?", (str(interaction.guild_id),))
        setup_data = self.cursor_setup.fetchone()
        if not setup_data or not interaction.user.get_role(int(setup_data["staff_role_id"])):
            print(f"ERROR: User {interaction.user.name} does not have permission to close ticket.")
            return await interaction.followup.send("You do not have permission to close this ticket.", ephemeral=True)
        confirm_view = ui.View()
        confirm_view.add_item(ui.Button(custom_id="yes_close", label="Yes", emoji="✅", style=discord.ButtonStyle.secondary))
        confirm_view.add_item(ui.Button(custom_id="no_close", label="No", emoji="❌", style=discord.ButtonStyle.secondary))
        await interaction.channel.send("Are you sure you want to close this ticket?", view=confirm_view)
        print(f"LOG: Close confirmation sent to channel {interaction.channel.id}.")

    async def handle_close_confirm(self, interaction: discord.Interaction, confirm: bool):
        await interaction.response.defer()
        print(f"LOG: Close confirmation received: {confirm} from {interaction.user.name} in channel {interaction.channel.id}.")
        if not confirm:
            await interaction.message.delete()
            print("LOG: Closing of ticket aborted by user.")
            return await interaction.followup.send("Closing of ticket aborted.", ephemeral=True)
        try:
            self.cursor_setup.execute("SELECT * FROM setup WHERE guild_id = ?", (str(interaction.guild_id),))
            setup_data = self.cursor_setup.fetchone()
            self.cursor_order_tickets.execute("SELECT * FROM tickets WHERE channel_id = ?", (str(interaction.channel.id),))
            ticket_data = self.cursor_order_tickets.fetchone()
            if not ticket_data:
                print(f"ERROR: Channel {interaction.channel.id} is not a valid ticket.")
                return await interaction.followup.send("❌ This channel is not a valid ticket.")
            ticket_user = await self.bot.fetch_user(ticket_data["user_id"])
            transcript_channel = self.bot.get_channel(int(setup_data["transcript_channel_id"]))
            if transcript_channel:
                transcript_messages = [m async for m in interaction.channel.history(limit=None, oldest_first=True)]
                transcript_content = "\n".join([f"[{m.created_at.strftime('%Y-%m-%d %H:%M:%S')}] {m.author.name}: {m.content}" for m in transcript_messages])
                transcript_file = discord.File(
                    io.StringIO(transcript_content),
                    filename=f"transcript-{interaction.channel.name}.txt"
                )
                transcript_embed = discord.Embed(
                    title="📒 Ticket Transcript",
                    description=f"Ticket for {ticket_user.mention} (`{ticket_user.id}`)",
                    color=discord.Color.blue()
                )
                await transcript_channel.send(embed=transcript_embed, file=transcript_file)
                print(f"LOG: Transcript sent to channel {transcript_channel.name}.")

            if ticket_data["ticket_type"] == "purchase" and setup_data["reviews_channel_id"]:
                reviews_channel = self.bot.get_channel(int(setup_data["reviews_channel_id"]))
                if reviews_channel:
                    try:
                        review_embed = discord.Embed(
                            title="⭐ Rate Your Experience!",
                            description="How was your experience with our service? Please leave a rating and feedback.",
                            color=discord.Color.gold()
                        )
                        review_view = RatingView(ticket_data["order_number"])
                        await ticket_user.send(embed=review_embed, view=review_view)
                        print(f"LOG: Review DM sent to user {ticket_user.id} for order {ticket_data['order_number']}.")
                    except Exception as dm_e:
                        print(f"ERROR: Failed to send review DM to user {ticket_user.id}: {dm_e}")

            self.cursor_order_tickets.execute("DELETE FROM tickets WHERE channel_id = ?", (str(interaction.channel.id),))
            self.conn_order_tickets.commit()
            print(f"LOG: Ticket deleted from '{ORDER_TICKETS_DB_NAME}' for channel {interaction.channel.id}.")
            await interaction.channel.delete(reason=f"Ticket closed by {interaction.user.name}")
            print(f"LOG: Channel {interaction.channel.id} deleted.")
        except Exception as e:
            print(f"ERROR: Error in handle_close_confirm: {e}")
            await interaction.followup.send(f"❌ An error occurred while closing the ticket: `{e}`")

    async def handle_claim_ticket(self, interaction):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' attempting to claim ticket in channel {interaction.channel.id}.")
        self.cursor_setup.execute("SELECT staff_role_id FROM setup WHERE guild_id = ?", (str(interaction.guild_id),))
        setup_data = self.cursor_setup.fetchone()
        if not setup_data or not interaction.user.get_role(int(setup_data["staff_role_id"])):
            print(f"ERROR: User {interaction.user.name} does not have permission to claim ticket.")
            return await interaction.followup.send("You do not have permission to claim this ticket.", ephemeral=True)
        self.cursor_order_tickets.execute("SELECT claimed_by_id FROM tickets WHERE channel_id = ?", (str(interaction.channel.id),))
        ticket_data = self.cursor_order_tickets.fetchone()
        if not ticket_data:
            print(f"ERROR: Channel {interaction.channel.id} is not a valid ticket for claiming.")
            return await interaction.followup.send("❌ This channel is not a valid ticket.")
        if ticket_data["claimed_by_id"] is not None:
            claimed_by = await self.bot.fetch_user(ticket_data["claimed_by_id"])
            print(f"LOG: Ticket already claimed by {claimed_by.name}.")
            return await interaction.followup.send(f"❌ This ticket has already been claimed by {claimed_by.mention}.", ephemeral=True)
        self.cursor_order_tickets.execute("UPDATE tickets SET claimed_by_id = ? WHERE channel_id = ?", (str(interaction.user.id), str(interaction.channel.id)))
        self.conn_order_tickets.commit()
        print(f"LOG: Ticket in channel {interaction.channel.id} claimed by {interaction.user.name} in '{ORDER_TICKETS_DB_NAME}'.")
        embed = discord.Embed(
            title="🎯 Ticket Claimed",
            description=f"This ticket has been claimed by {interaction.user.mention}",
            color=discord.Color.green()
        )
        embed.set_footer(text=f"Claimed by {interaction.user.name}", icon_url=interaction.user.display_avatar.url)
        await interaction.channel.send(embed=embed)
        await interaction.followup.send("✅ You have successfully claimed this ticket!", ephemeral=True)
        print(f"LOG: Ticket claimed confirmation sent to {interaction.user.name}.")
        
    async def handle_transcript_ticket(self, interaction):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' requested transcript for channel {interaction.channel.id}.")
        self.cursor_setup.execute("SELECT transcript_channel_id FROM setup WHERE guild_id = ?", (str(interaction.guild_id),))
        setup_data = self.cursor_setup.fetchone()
        if not setup_data or not setup_data["transcript_channel_id"]:
            print("ERROR: Transcript channel not configured.")
            return await interaction.followup.send("Transcript channel is not configured.", ephemeral=True)
        transcript_channel = self.bot.get_channel(int(setup_data["transcript_channel_id"]))
        if not transcript_channel:
            print(f"ERROR: Transcript channel {setup_data['transcript_channel_id']} not found.")
            return await interaction.followup.send("Transcript channel not found.", ephemeral=True)
        messages = []
        async for message in interaction.channel.history(limit=None, oldest_first=True):
            if not message.author.bot or message.embeds or message.attachments:
                timestamp = message.created_at.strftime("%Y-%m-%d %H:%M:%S")
                content = message.content or "*[Embed/Attachment]*"
                messages.append(f"[{timestamp}] {message.author.name}: {content}")
        transcript_content = "\n".join(messages)
        transcript_file = io.StringIO(transcript_content)
        file = discord.File(transcript_file, filename=f"transcript-{interaction.channel.name}.txt")
        embed = discord.Embed(
            title="📒 Ticket Transcript",
            description=f"Transcript for #{interaction.channel.name}",
            color=discord.Color.blue()
        )
        embed.add_field(name="Channel", value=interaction.channel.mention, inline=True)
        embed.add_field(name="Generated by", value=interaction.user.mention, inline=True)
        embed.add_field(name="Messages", value=len(messages), inline=True)
        await transcript_channel.send(embed=embed, file=file)
        await interaction.followup.send("✅ Transcript has been generated and sent to the transcript channel!", ephemeral=True)
        print(f"LOG: Transcript sent to {transcript_channel.name}.")

    async def handle_show_supporters(self, interaction):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' requested to show supporters.")
        self.cursor_setup.execute("SELECT supporter_role_ids FROM setup WHERE guild_id = ?", (str(interaction.guild_id),))
        setup_data = self.cursor_setup.fetchone()
        if not setup_data or not setup_data["supporter_role_ids"]:
            print("LOG: No supporter roles configured.")
            return await interaction.followup.send("No supporter roles configured.", ephemeral=True)
        supporter_role_ids = json.loads(setup_data["supporter_role_ids"])
        supporters = []
        for role_id in supporter_role_ids:
            role = interaction.guild.get_role(int(role_id))
            if role:
                online_members = [member for member in role.members if member.status != discord.Status.offline]
                supporters.append(f"**{role.name}:** {len(online_members)} online, {len(role.members)} total")
        embed = discord.Embed(
            title="👥 Support Team",
            description="\n".join(supporters) if supporters else "No supporters found.",
            color=discord.Color.blue()
        )
        await interaction.followup.send(embed=embed, ephemeral=True)
        print("LOG: Supporters list sent.")

    async def handle_show_pricelist(self, interaction):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' requested to show pricelist.")
        self.cursor_products.execute("SELECT * FROM products WHERE is_active = 1 ORDER BY price ASC")
        products = self.cursor_products.fetchall()
        if not products:
            print("LOG: No products available for pricelist display.")
            return await interaction.followup.send("❌ No products available at the moment.")
        embed = discord.Embed(
            color=0x5865F2,
            title="✨ Our Premium Services",
            description="Choose from our high-quality offers:",
        )
        embed.set_thumbnail(url=NEW_IMAGE_URL)
        for product in products:
            emoji_to_use = "🛒"
            if product['emoji'] and validate_emoji(product['emoji']):
                emoji_to_use = product['emoji']
            embed.add_field(
                name=f"{emoji_to_use} {product['name']}",
                value=f"```€{product['price']:.2f}```\n{product['description'] or 'Professional service'}\n✅ High Quality\n✅ Fast Delivery\n✅ 24/7 Support",
                inline=True
            )
        embed.set_footer(text="Satisfaction guarantee | 24/7 Support", icon_url=NEW_IMAGE_URL)
        view = ui.View()
        view.add_item(ui.Button(custom_id="startOrder", label="Order Now →", style=discord.ButtonStyle.green))
        await interaction.followup.send(embed=embed, view=view)
        print("LOG: Pricelist displayed.")

    async def handle_start_order(self, interaction):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' starting a new order.")
        try:
            order_number = generate_short_id()
            items = json.dumps([])
            self.cursor_order_tickets.execute("INSERT INTO orders (user_id, order_number, items, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
                (str(interaction.user.id), order_number, items, datetime.datetime.now().isoformat(), datetime.datetime.now().isoformat()))
            self.conn_order_tickets.commit()
            print(f"LOG: New order {order_number} created in '{ORDER_TICKETS_DB_NAME}'.")
            self.cursor_products.execute("SELECT * FROM products WHERE is_active = 1 ORDER BY price ASC")
            products = self.cursor_products.fetchall()
            if not products:
                print("LOG: No products available for ordering.")
                return await interaction.followup.send("❌ No products available for ordering.")
            options = []
            for product in products:
                emoji_to_use = "🛒"
                if product['emoji'] and validate_emoji(product['emoji']):
                    emoji_to_use = product['emoji']
                options.append(discord.SelectOption(
                    label=f"{product['name']} (€{product['price']:.2f})",
                    value=product['product_key'],
                    emoji=emoji_to_use,
                    description=product['description'][:100] if product['description'] else "Professional service"
                ))
            select_menu = ui.Select(
                custom_id="selectService",
                placeholder="Select a service...",
                options=options
            )
            view = ui.View()
            view.add_item(select_menu)
            await interaction.followup.send("**Step 1/2**: Select your service:", view=view)
            print("LOG: Service selection menu sent.")
        except Exception as e:
            print(f"ERROR: Error in startOrder handler: {e}")
            await interaction.followup.send(f"❌ An error occurred while starting the order: `{e}`")

    async def handle_products_dropdown_select(self, interaction):
        await interaction.response.defer(ephemeral=True)
        selected_product_key = interaction.data["values"][0]
        print(f"LOG: Product dropdown selected: {selected_product_key} by {interaction.user.name}.")
        try:
            self.cursor_products.execute("SELECT * FROM products WHERE product_key = ? AND is_active = 1", (selected_product_key,))
            selected_product = self.cursor_products.fetchone()
            if not selected_product:
                print(f"ERROR: Invalid product selected from dropdown: {selected_product_key}.")
                return await interaction.followup.send("❌ Invalid product selected.", ephemeral=True)
            
            emoji_to_use = "❓"
            if selected_product['emoji'] and validate_emoji(selected_product['emoji']):
                emoji_to_use = selected_product['emoji']
                
            product_embed = discord.Embed(
                title=f"{emoji_to_use} {selected_product['name']}",
                description=selected_product['description'] or "Professional service with high quality standards.",
                color=discord.Color.blurple()
            )
            product_embed.add_field(name="💰 Price", value=f"€{selected_product['price']:.2f}", inline=True)
            product_embed.add_field(name="🚀 Delivery", value="1-3 business days", inline=True)
            product_embed.add_field(name="✅ Quality", value="Premium guaranteed", inline=True)
            product_embed.set_footer(text="To proceed with this purchase, please create a purchase ticket via the main ticket menu.")
            product_embed.set_thumbnail(url=NEW_IMAGE_URL)
            await interaction.followup.send(embed=product_embed)
            print(f"LOG: Product details for {selected_product_key} sent.")
        except Exception as e:
            print(f"ERROR: Error in products dropdown select handler: {e}")
            await interaction.followup.send(f"❌ An error occurred while processing your product selection: `{e}`", ephemeral=True)

    async def handle_select_payment(self, interaction):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' attempting to select payment.")
        await interaction.followup.send("Payment selection is not fully implemented yet.", ephemeral=True)

    async def handle_add_more_services(self, interaction):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' attempting to add more services.")
        await interaction.followup.send("Add more services is not fully implemented yet.", ephemeral=True)

    async def handle_apply_discount_modal(self, interaction):
        print(f"LOG: '{interaction.user.name}' opening ApplyDiscountModal.")
        await interaction.response.send_modal(ApplyDiscountModal(self))

    async def handle_apply_discount_modal_submit(self, interaction, code):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' submitting ApplyDiscountModal with code: {code}.")
        try:
            code = code.upper()
            self.cursor_order_tickets.execute("SELECT * FROM tickets WHERE channel_id = ?", (str(interaction.channel.id),))
            ticket_data = self.cursor_order_tickets.fetchone()
            if not ticket_data:
                print(f"ERROR: Channel {interaction.channel.id} is not a valid ticket channel for discount application.")
                return await interaction.followup.send("❌ This is not a valid ticket channel.")

            order_number = ticket_data["order_number"]
            self.cursor_order_tickets.execute("SELECT * FROM orders WHERE order_number = ?", (order_number,))
            order_data = self.cursor_order_tickets.fetchone()
            if not order_data:
                print(f"ERROR: No active order found for ticket {ticket_data['channel_id']} to apply discount.")
                return await interaction.followup.send("❌ No active order found for this ticket.", ephemeral=True)

            self.cursor_discounts.execute("SELECT * FROM discounts WHERE code = ? AND is_active = 1 AND expires_at > ?", 
                (code, datetime.datetime.now().isoformat()))
            discount_data = self.cursor_discounts.fetchone()
            if not discount_data:
                print(f"ERROR: Invalid or expired discount code: {code}.")
                return await interaction.followup.send("❌ Invalid or expired discount code.")


            if discount_data["max_uses"] and discount_data["used_count"] >= discount_data["max_uses"]:
                print(f"ERROR: Discount code {code} reached its total usage limit.")
                return await interaction.followup.send("❌ This discount code has reached its usage limit.")


            self.cursor_discounts.execute("SELECT COUNT(*) FROM discount_usage WHERE discount_code = ? AND user_id = ?", (code, str(interaction.user.id)))
            user_usage_count = self.cursor_discounts.fetchone()[0]

            if discount_data['usage_type'] == 'single':
                if user_usage_count > 0:
                    return await interaction.followup.send("❌ You have already used this discount code once.", ephemeral=True)
            elif discount_data['usage_type'] == 'multiple' and discount_data['max_uses_per_user'] is not None:
                if user_usage_count >= discount_data['max_uses_per_user']:
                    return await interaction.followup.send(f"❌ You have already used this discount code the maximum of {discount_data['max_uses_per_user']} times.", ephemeral=True)


            applies_to_products = json.loads(discount_data['applies_to']) if discount_data['applies_to'] else []
            order_items = json.loads(order_data['items'])
            if applies_to_products:
                order_product_keys = {item.get('product_key') for item in order_items if item.get('product_key')}
                if not any(pk in applies_to_products for pk in order_product_keys):
                    print(f"ERROR: Discount code {code} does not apply to products in order {order_data['order_number']}.")
                    return await interaction.followup.send("❌ This discount code does not apply to the products in your current order.", ephemeral=True)


            new_total = order_data["subtotal"] * (1 - discount_data["percent"] / 100)
            self.cursor_order_tickets.execute("UPDATE orders SET discount_code = ?, discount_amount = ?, total_amount = ? WHERE order_number = ?",
                (discount_data["code"], discount_data["percent"], new_total, order_data["order_number"]))
            

            self.cursor_discounts.execute("UPDATE discounts SET used_count = used_count + 1 WHERE code = ?", (discount_data["code"],))
            

            self.cursor_discounts.execute("INSERT INTO discount_usage (order_number, user_id, discount_code, used_at) VALUES (?, ?, ?, ?)",
                (order_data["order_number"], str(interaction.user.id), discount_data["code"], datetime.datetime.now().isoformat()))

            self.conn_order_tickets.commit()
            self.conn_discounts.commit()
            print(f"LOG: Discount applied to order {order_data['order_number']}: Code={discount_data['code']}, New Total={new_total}.")
            
            try:
                original_message = await interaction.channel.fetch_message(ticket_data["ticket_message_id"])
                original_embed = original_message.embeds[0]
                
                for i, field in enumerate(original_embed.fields):
                    if field.name == "💰 Price":
                        original_embed.set_field_at(
                            i, 
                            name="💰 Price", 
                            value=f"~~€{order_data['subtotal']:.2f}~~ **€{new_total:.2f}**", 
                            inline=True
                        )
                        break
                await original_message.edit(embed=original_embed)
            except Exception as e:
                print(f"ERROR: Could not edit original ticket embed: {e}")

            success_embed = discord.Embed(
                title="✅ Discount Applied!",
                description=f"**{discount_data['code']}** - {discount_data['percent']}% off",
                color=0x57F287
            )
            success_embed.add_field(name="Original Total", value=f"€{order_data['subtotal']:.2f}", inline=True)
            success_embed.add_field(name="Discount", value=f"-€{(order_data['subtotal'] * (discount_data['percent'] / 100)):.2f}", inline=True)
            success_embed.add_field(name="New Total", value=f"€{new_total:.2f}", inline=True)
            await interaction.followup.send(embed=success_embed)
            print(f"LOG: Discount application confirmation sent for order {order_data['order_number']}.")
        except Exception as e:
            print(f"ERROR: Error in discount modal submit handler: {e}")
            await interaction.followup.send(f"❌ An error occurred while applying the discount: `{e}`")

    async def handle_remove_discount(self, interaction):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' attempting to remove discount in channel {interaction.channel.id}.")
        try:
            self.cursor_order_tickets.execute("SELECT * FROM tickets WHERE channel_id = ?", (str(interaction.channel.id),))
            ticket_data = self.cursor_order_tickets.fetchone()

            if not ticket_data or not ticket_data["order_number"]:
                print(f"ERROR: Could not find a ticket or associated order for channel {interaction.channel.id}.")
                return await interaction.followup.send("❌ This ticket is not associated with an order.", ephemeral=True)
            
            order_number = ticket_data["order_number"]

            self.cursor_order_tickets.execute("SELECT * FROM orders WHERE order_number = ?", (order_number,))
            order_data = self.cursor_order_tickets.fetchone()
            
            if not order_data or not order_data["discount_code"]:
                print(f"LOG: No discount code applied to order {order_number} to remove.")
                return await interaction.followup.send("❌ No discount code is applied to this order.", ephemeral=True)

            discount_code_to_remove = order_data["discount_code"]


            self.cursor_order_tickets.execute("UPDATE orders SET discount_code = NULL, discount_amount = 0, total_amount = subtotal WHERE order_number = ?",
                (order_data["order_number"],))
            

            self.cursor_discounts.execute("UPDATE discounts SET used_count = used_count - 1 WHERE code = ? AND used_count > 0", (discount_code_to_remove,))
            

            self.cursor_discounts.execute("DELETE FROM discount_usage WHERE order_number = ? AND user_id = ? AND discount_code = ?",
                (order_number, str(interaction.user.id), discount_code_to_remove))
            
            self.conn_order_tickets.commit()
            self.conn_discounts.commit()
            
            print(f"LOG: Discount '{discount_code_to_remove}' removed from order {order_data['order_number']}.")
            await interaction.followup.send(f"✅ Discount code `{discount_code_to_remove}` has been removed from your order.")

        except Exception as e:
            print(f"ERROR: Error in remove_discount handler: {e}")
            await interaction.followup.send(f"❌ An error occurred while removing the discount: `{e}`", ephemeral=True)

    async def handle_final_confirm(self, interaction):
        await interaction.response.defer()
        print(f"LOG: '{interaction.user.name}' confirming final order.")
        try:
            self.cursor_order_tickets.execute("SELECT * FROM orders WHERE user_id = ? ORDER BY created_at DESC", (str(interaction.user.id),))
            order_data = self.cursor_order_tickets.fetchone()
            if not order_data:
                print(f"ERROR: No order found for user {interaction.user.id} during final confirmation.")
                return await interaction.followup.send("❌ No order found.")
            payment_method = "PayPal"
            self.cursor_order_tickets.execute("INSERT INTO payments (user_id, order_id, order_number, method, amount, created_at) VALUES (?, ?, ?, ?, ?, ?)",
                (str(interaction.user.id), order_data["order_id"], order_data["order_number"], payment_method, order_data["total_amount"], datetime.datetime.now().isoformat()))
            self.conn_order_tickets.commit()
            print(f"LOG: Payment recorded in '{ORDER_TICKETS_DB_NAME}': Order ID={order_data['order_id']}, Amount={order_data['total_amount']}.")
            history = json.dumps([{"status": "processing", "changed_at": datetime.datetime.now().isoformat(), "changed_by": str(interaction.user.id)}])
            self.cursor_order_tickets.execute("INSERT INTO tracking (order_id, order_number, channel_id, status_message_id, ticket_message_id, history, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (order_data["order_id"], order_data["order_number"], str(interaction.channel_id), None, None, history, datetime.datetime.now().isoformat(), datetime.datetime.now().isoformat()))
            self.conn_order_tickets.commit()
            print(f"LOG: Tracking record created in '{ORDER_TICKETS_DB_NAME}': Order ID={order_data['order_id']}, Channel ID={interaction.channel_id}.")
            success_embed = discord.Embed(
                color=0x57F287,
                title="✅ Order Complete!",
                description="Thank you for your order!"
            )
            success_embed.add_field(name="Order Number", value=f"#{order_data['order_number']}", inline=True)
            success_embed.add_field(name="Total Amount", value=f"€{order_data['total_amount']:.2f}", inline=True)
            success_embed.add_field(name="Payment Method", value=payment_method, inline=True)
            success_embed.add_field(name="Payment Details", value=get_payment_instructions(payment_method.lower(), order_data['order_number'], order_data['total_amount']))
            success_embed.set_thumbnail(url=NEW_IMAGE_URL)
            view = OrderCompleteView(has_reviews_channel=True)
            await interaction.followup.send(embed=success_embed, view=view, ephemeral=True)
            print("LOG: Order complete message sent.")
            status_embed = await create_status_embed(order_data, "processing")
            status_message = await interaction.channel.send(embed=status_embed)
            self.cursor_order_tickets.execute("UPDATE tracking SET status_message_id = ? WHERE order_number = ?", (str(status_message.id), order_data["order_number"]))
            self.conn_order_tickets.commit()
            print(f"LOG: Tracking message ID updated for order {order_data['order_number']} in '{ORDER_TICKETS_DB_NAME}': Message ID={status_message.id}.")
        except Exception as e:
            print(f"ERROR: Error in final_confirm handler: {e}")
            await interaction.followup.send(f"❌ An error occurred while confirming the order: `{e}`")

    async def update_all_status_embeds(self, client, order_number, new_status, user, note_message=None):
        print(f"LOG: Attempting to update status embeds for order {order_number} to {new_status}.")
        self.cursor_order_tickets.execute("SELECT * FROM orders WHERE order_number = ?", (order_number,))
        order_data = self.cursor_order_tickets.fetchone()
        if not order_data:
            print(f"ERROR: Order {order_number} not found for status embed update.")
            return {"success": False, "message": "Order not found"}
        self.cursor_order_tickets.execute("SELECT * FROM tracking WHERE order_number = ?", (order_number,))
        tracking_data = self.cursor_order_tickets.fetchone()
        if not tracking_data:
            print(f"ERROR: Tracking data not found for order {order_number}.")
            return {"success": False, "message": "Tracking not found"}
        embed = await create_status_embed(order_data, new_status)
        try:
            channel = await client.fetch_channel(int(tracking_data["channel_id"]))
            status_message = await channel.fetch_message(int(tracking_data["status_message_id"]))
            await status_message.edit(embed=embed)
            print(f"LOG: Status embed updated for order {order_number} in channel {channel.id}.")
        except (NotFound, ValueError) as e:
            print(f"ERROR: Error updating status message for order {order_number}: {e}")
        try:
            status_embed = discord.Embed(
                title=f"📦 Order Status Updated: #{order_number}",
                description=f"Hello {user.mention}, your order status has been updated to **{format_status(new_status)}**!",
                color=get_status_color(new_status)
            )
            items_list = json.loads(order_data['items'])
            items_value = "\n".join([f"• {item['name']} (€{item['price']:.2f})" for item in items_list]) if items_list else "No items"
            status_embed.add_field(name="Order Details", value=items_value, inline=False)
            status_embed.add_field(name="Current Status", value=f"**{format_status(new_status)}**", inline=False)
            if note_message:
                status_embed.add_field(name="Admin Note", value=note_message, inline=False)
            status_embed.set_footer(text="Thank you for your business!", icon_url=NEW_IMAGE_URL)
            status_embed.timestamp = datetime.datetime.now()
            await user.send(embed=status_embed)
            print(f"LOG: Status update direct message sent to user {user.id}.")
        except NotFound:
            print(f"ERROR: User {user.id} not found for status update DM.")
        except Exception as e:
            print(f"ERROR: Failed to send status update DM to user {user.id}: {e}")
        try:
            self.cursor_setup.execute("SELECT status_channel_id FROM setup WHERE guild_id = ?", (channel.guild.id,))
            status_channel_id = self.cursor_setup.fetchone()
            if status_channel_id and status_channel_id["status_channel_id"]:
                status_channel = self.bot.get_channel(int(status_channel_id["status_channel_id"]))
                if status_channel:
                    status_log_embed = discord.Embed(
                        title=f"Order Status Update: #{order_number}",
                        description=f"Status changed to **{format_status(new_status)}**",
                        color=get_status_color(new_status)
                    )
                    status_log_embed.add_field(name="Customer", value=f"<@{user.id}>", inline=True)
                    status_log_embed.add_field(name="Updated by", value=f"<@{user.id}>", inline=True)
                    if note_message:
                        status_log_embed.add_field(name="Admin Note", value=note_message, inline=False)
                    status_log_embed.timestamp = datetime.datetime.now()
                    await status_channel.send(embed=status_log_embed)
                    print(f"LOG: Status update sent to debugging/logging channel {status_channel.id}.")
        except Exception as e:
            print(f"ERROR: Failed to send status update to dedicated channel: {e}")

    async def handle_cancel_order(self, interaction):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' attempting to cancel order.")
        try:
            confirm_embed = discord.Embed(
                color=0xED4245,
                title="⚠️ Are you sure you want to cancel the order?",
                description="This action cannot be undone!"
            )
            confirm_view = CancelConfirmView()
            await interaction.followup.send(embed=confirm_embed, view=confirm_view, ephemeral=True)
            print("LOG: Order cancellation confirmation sent.")
            await confirm_view.wait()
            if confirm_view.value:
                self.cursor_order_tickets.execute("SELECT * FROM orders WHERE user_id = ? ORDER BY created_at DESC", (str(interaction.user.id),))
                order_data = self.cursor_order_tickets.fetchone()
                if order_data:
                    order_number = order_data["order_number"]
                    self.cursor_order_tickets.execute("UPDATE orders SET status = 'cancelled' WHERE order_number = ?", (order_number,))
                    self.cursor_order_tickets.execute("UPDATE payments SET status = 'refunded' WHERE order_number = ?", (order_number,))
                    self.cursor_order_tickets.execute("UPDATE tracking SET status = 'cancelled' WHERE order_number = ?", (order_number,))
                    self.conn_order_tickets.commit()
                    print(f"LOG: Order {order_number} cancelled and related records updated in '{ORDER_TICKETS_DB_NAME}'.")
                    await interaction.followup.send("✅ Order has been successfully cancelled.", ephemeral=True)
                    await self.update_all_status_embeds(interaction.client, order_number, "cancelled", interaction.user)
                    print(f"LOG: Order cancellation confirmation sent for order {order_number}.")
                else:
                    print(f"LOG: No order found for user {interaction.user.id} to cancel.")
                    await interaction.followup.send("❌ No order found to cancel.", ephemeral=True)
            else:
                print("LOG: Order cancellation aborted by user.")
                await interaction.followup.send("Cancellation aborted.", ephemeral=True)
        except Exception as e:
            print(f"ERROR: Error in cancel_order handler: {e}")
            await interaction.followup.send(f"❌ An error occurred while canceling the order: `{e}`")

    async def handle_generate_invoice(self, interaction):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' requested invoice generation.")
        try:
            self.cursor_order_tickets.execute("SELECT * FROM orders WHERE user_id = ? ORDER BY created_at DESC", (str(interaction.user.id),))
            order_data = self.cursor_order_tickets.fetchone()
            if not order_data:
                print(f"ERROR: Order not found for user {interaction.user.id} for invoice generation.")
                return await interaction.followup.send("Order not found.")
            file_path = generate_pdf_invoice(order_data)
            await interaction.followup.send(file=discord.File(file_path))
            os.remove(file_path)
            print(f"LOG: Invoice generated and sent for order {order_data['order_number']}.")
        except Exception as e:
            print(f"ERROR: Error in generate_invoice handler: {e}")
            await interaction.followup.send(f"❌ An error occurred while generating the invoice: `{e}`")

    @app_commands.command(name="list-orders", description="Lists all active orders with their status.")
    @app_commands.checks.has_permissions(administrator=True)
    async def list_orders(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' requested a list of all orders.")
        try:
            self.cursor_order_tickets.execute("SELECT order_number, user_id, status, created_at FROM orders")
            orders = self.cursor_order_tickets.fetchall()
            if not orders:
                return await interaction.followup.send("❌ No orders found in the database.")
            embed = discord.Embed(
                title="📦 Active Orders List",
                description="List of all orders and their current status.",
                color=discord.Color.blue()
            )
            for order in orders:
                user = await self.bot.fetch_user(order['user_id'])
                embed.add_field(
                    name=f"Order ID: `{order['order_number']}`",
                    value=f"**Customer:** {user.mention if user else 'Unknown User'}\n**Status:** `{order['status']}`\n**Created At:** {order['created_at']}",
                    inline=False
                )
            await interaction.followup.send(embed=embed)
            print("LOG: Orders list sent successfully.")
        except Exception as e:
            print(f"ERROR: Error listing orders: {e}")
            await interaction.followup.send(f"❌ An error occurred while listing the orders: `{e}`")

    @app_commands.command(name="set-order-updates", description="Sets a channel for all order status updates.")
    @app_commands.checks.has_permissions(administrator=True)
    @app_commands.describe(
        channel="The channel to send status update logs to.",
    )
    async def set_order_updates(self, interaction: discord.Interaction, channel: discord.TextChannel):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' setting status update channel to {channel.name}.")
        try:
            self.cursor_setup.execute("UPDATE setup SET status_channel_id = ? WHERE guild_id = ?", (str(channel.id), str(interaction.guild_id)))
            self.conn_setup.commit()
            print(f"LOG: Status update channel configured for guild {interaction.guild.id} in 'setup_config.db'.")
            await interaction.followup.send(f"✅ Order status updates will now be sent to {channel.mention} for administrative review.")
        except Exception as e:
            print(f"ERROR: Error in set-order-updates command: {e}")
            await interaction.followup.send(f"❌ An error occurred while setting the status channel: `{e}`")

    async def handle_check_status(self, interaction):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' requested to check order status.")
        try:
            self.cursor_order_tickets.execute("SELECT * FROM orders WHERE user_id = ? ORDER BY created_at DESC", (str(interaction.user.id),))
            order_data = self.cursor_order_tickets.fetchone()
            if not order_data:
                print(f"LOG: No orders found for user {interaction.user.id}.")
                return await interaction.followup.send("❌ No orders found.")
            self.cursor_order_tickets.execute("SELECT * FROM tracking WHERE order_id = ?", (order_data["order_id"],))
            tracking_data = self.cursor_order_tickets.fetchone()
            if not tracking_data:
                print(f"ERROR: Tracking information not found for order {order_data['order_id']}.")
                return await interaction.followup.send("Tracking information not found.")
            status_embed = await create_status_embed(order_data, tracking_data["status"])
            await interaction.followup.send(embed=status_embed)
            print(f"LOG: Order status sent for order {order_data['order_number']}.")
        except Exception as e:
            print(f"ERROR: Error in check_status handler: {e}")
            await interaction.followup.send(f"❌ An error occurred while checking the status: `{e}`")

    async def handle_rate_service_stars(self, interaction, stars, order_number):
        print(f"LOG: '{interaction.user.name}' attempting to rate service with {stars} stars for order {order_number}.")
        try:
            self.cursor_order_tickets.execute("SELECT order_number FROM orders WHERE user_id = ? ORDER BY created_at DESC", (str(interaction.user.id),))
            ticket_data = self.cursor_order_tickets.fetchone()
            if not ticket_data:
                print(f"ERROR: No ticket found for user {interaction.user.id} to rate.")
                await interaction.response.defer(ephemeral=True)
                return await interaction.followup.send("❌ No active ticket found to rate.", ephemeral=True)
            
            modal = ui.Modal(title="Additional Feedback")
            modal.custom_id = f"feedback_modal_{order_number}_{stars}"
            feedback_input = ui.TextInput(label="Your feedback (optional)", custom_id="feedback_text", style=discord.TextStyle.long, required=False)
            modal.add_item(feedback_input)
            
            await interaction.response.send_modal(modal)
            print("LOG: Feedback modal sent.")
        except Exception as e:
            print(f"ERROR: Error in rate_service handler: {e}")
            await interaction.response.defer(ephemeral=True)
            await interaction.followup.send(f"❌ An error occurred while rating the service: `{e}`")
    
    async def handle_feedback_modal_submit(self, interaction, stars, order_number):
        await interaction.response.defer(ephemeral=True)
        print(f"LOG: '{interaction.user.name}' submitting feedback modal with stars: {stars} for order {order_number}.")
        try:
            feedback = interaction.data['components'][0]['components'][0]['value']
            
            self.cursor_order_tickets.execute("SELECT guild_id FROM orders WHERE order_number = ?", (order_number,))
            order_guild_data = self.cursor_order_tickets.fetchone()

            if not order_guild_data or not order_guild_data["guild_id"]:
                print(f"ERROR: Could not find guild_id for order {order_number} in the database.")
                return await interaction.followup.send("Could not associate this order with a server. Review cannot be posted.", ephemeral=True)

            guild_id = order_guild_data["guild_id"]
            
            self.cursor_setup.execute("SELECT reviews_channel_id FROM setup WHERE guild_id = ?", (guild_id,))
            setup_data = self.cursor_setup.fetchone()

            if not setup_data or not setup_data["reviews_channel_id"]:
                print(f"ERROR: Reviews channel not configured for guild_id: {guild_id}")
                return await interaction.followup.send("Reviews channel is not configured. - Thanks for trying tho :D", ephemeral=True)
            
            reviews_channel_id = setup_data["reviews_channel_id"]
            
            guild = self.bot.get_guild(int(guild_id))
            if not guild:
                print(f"ERROR: Bot is not in the guild with ID {guild_id} anymore.")
                return await interaction.followup.send("Cannot find the original server to post the review.", ephemeral=True)

            reviews_channel = guild.get_channel(int(reviews_channel_id))
            if not reviews_channel:
                print(f"ERROR: Reviews channel {reviews_channel_id} not found in guild {guild.name}.")
                return await interaction.followup.send("Reviews channel not found on the server.", ephemeral=True)
            
            self.cursor_order_tickets.execute("SELECT items FROM orders WHERE order_number = ?", (order_number,))
            order_data = self.cursor_order_tickets.fetchone()
            items_list = json.loads(order_data['items'])
            ordered_items = "\n".join([f"• {item['name']}" for item in items_list]) if items_list else "No items specified"

            review_embed = discord.Embed(
                color=0xFFD700,
                title=f"New Review: {'⭐' * stars}{'☆' * (5 - stars)}"
            )
            review_embed.description = feedback or "*No additional feedback provided*"
            review_embed.add_field(name="Customer", value=interaction.user.mention, inline=True)
            review_embed.add_field(name="Rating", value=f"{stars}/5", inline=True)
            review_embed.add_field(name="Order Number", value=f"`{order_number}`", inline=True)
            review_embed.add_field(name="Ordered Items", value=ordered_items, inline=False)
            review_embed.set_thumbnail(url=interaction.user.display_avatar.url)
            review_embed.timestamp = datetime.datetime.now()
            await reviews_channel.send(embed=review_embed)
            await interaction.followup.send(f"✅ Thank you for your {stars}-star rating!", ephemeral=True)
            print(f"LOG: Review submitted by {interaction.user.name} for order {order_number} with {stars} stars.")
        except Exception as e:
            print(f"ERROR: Error in feedback_modal_submit handler: {e}")
            await interaction.followup.send(f"❌ An error occurred while submitting feedback: `{e}`")

async def main():
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix="!", intents=intents)
    await bot.add_cog(OrderSystem(bot))
    try:
        with open('config.json') as f:
            config = json.load(f)
        TOKEN = config.get("TOKEN")
    except FileNotFoundError:
        print("Error: config.json file not found. Please create one with your bot token.")
        return
    except json.JSONDecodeError:
        print("Error: Invalid JSON in config.json file.")
        return
    
    if not TOKEN:
        print("Error: Bot token not found. Please set a 'TOKEN' in config.json")
        return
    if not os.path.exists('logs'):
        os.makedirs('logs')
    log_file_path = "logs/bot.log"
    try:
        log_file = open(log_file_path, "a", encoding='utf-8')
        original_stdout = sys.stdout
        original_stderr = sys.stderr
        sys.stdout = Tee(original_stdout, log_file)
        sys.stderr = Tee(original_stderr, log_file)

        await bot.start(TOKEN)
    except discord.errors.LoginFailure:
        print("Error: Invalid bot token. Please check your config.json file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if 'log_file' in locals() and not log_file.closed:
            log_file.close()
        if 'original_stdout' in locals():
            sys.stdout = original_stdout
        if 'original_stderr' in locals():
            sys.stderr = original_stderr
        if bot:
            await bot.close()



if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(license_text)
        print("Bot shutdown requested by user.")


"""
Custom License — August 8, 2025
Copyright (c) 2025 TheHolyOneZ

This license applies to:
- All files in this project directory and its subdirectories, including but not limited to all Python (*.py) files.
- All versions and components of the "ordersystem", including any file containing code, logic, or functionality originally created by TheHolyOneZ, whether in whole or in part.



Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated files (the “Software”), to use the Software only under the following conditions:

The Software may be run/executed.

Emojis in the Software’s interface may be changed.

No other modifications are allowed without prior written permission from the copyright holder.

The name of the Software, any usernames, or any branding (including but not limited to “TheHolyOneZ”, “TheZ”, and “ZygnalBot”) may not be changed.

The Software may not be transferred, redistributed, sublicensed, sold, or given to any third party.

No code snippets, components, or portions of the Software may be extracted for use in other projects.

The Software may not be copied, reproduced, or made publicly accessible except by the copyright holder.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

License Agreement (By Running it)
Issued to: TheHolyOneZ
Date: 08 August 2025

1. Definitions
This License Agreement (hereinafter the “License”) governs the use of the software/bot created by TheHolyOneZ (hereinafter the “Author”).

2. Permitted Actions
a) The Licensee may run/execute the bot.
b) The Licensee may change emojis in the bot’s interface.
c) No other functional or structural changes are allowed without the Author’s prior written consent.

3. Prohibited Actions
Without the Author’s prior written permission, the Licensee may not:
a) Change the bot’s name, username, project name, or any branding/labels associated with the software — including (but not limited to) “TheHolyOneZ”, “TheZ”, or “ZygnalBot”.
b) Transfer, resell, gift, sublicense, or otherwise distribute the bot to any third party.
c) Extract code snippets, segments, or entire portions of the software for use in other projects, repositories, or products.
d) Copy, reproduce, or make the bot publicly accessible in any form.

4. Ownership and Copyright
All rights, including copyright and all related intellectual property rights, remain solely with the Author TheHolyOneZ.

5. Disclaimer and Warranty
The software is provided “as is” without any warranty of any kind, express or implied. The Author shall not be liable for any damages, including but not limited to loss of profit, data loss, or other indirect damages arising from the use of the software.

6. Term and Termination
This License takes effect on the above date and remains valid until revoked in writing by the Author.
If the Licensee violates Section 3, this License terminates immediately, and the Licensee must delete the software and destroy all copies.

7. Governing Law and Jurisdiction
Where legally permissible, this License is governed by the laws of Germany. The place of jurisdiction shall be the Author’s location.

8. Miscellaneous
Any amendments or additions to this License require written form and the explicit consent of the Author.
"""


